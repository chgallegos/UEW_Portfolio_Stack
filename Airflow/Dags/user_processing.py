from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

import json
from pandas import json_normalize
from datetime import datetime

# Function to process the user data extracted from the API
def _process_user(ti):
    # Pull user data from the previous task's XCom
    user = ti.xcom_pull(task_ids="extract_user")
    user = user['results'][0]  # Extract the first user from the response
    # Normalize the user data into a flat structure and save it as a CSV file
    processed_user = json_normalize({
        'firstname': user['name']['first'],
        'lastname': user['name']['last'],
        'country': user['location']['country'],
        'username': user['login']['username'],
        'password': user['login']['password'],
        'email': user['email']})
    processed_user.to_csv('/tmp/processed_user.csv', index=None, header=False)

# Function to store the processed user data into a PostgreSQL database
def _store_user():
    hook = PostgresHook(postgres_conn_id='postgres')  # Connect to Postgres
    # Use copy_expert to copy the CSV data into the database
    hook.copy_expert(
        sql="COPY users FROM stdin WITH DELIMITER as ','",
        filename='/tmp/processed_user.csv'
    )

# Define the DAG
with DAG(
    'user_processing',  # Unique identifier for the DAG
    start_date=datetime(2025, 1, 1),  # Start scheduling from this date
    schedule_interval='@daily',  # Run daily
    catchup=False  # Do not backfill past runs
) as dag:
    
    # Task to create the users table in the Postgres database
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',  # Connection ID for Postgres
        sql='''
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            );
        '''
    )

    # Task to check if the user API is available
    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='user_api',  # Connection ID for the API
        endpoint='api/'  # API endpoint to check availability
    )

    # Task to extract user data from the API
    extract_user = SimpleHttpOperator(
        task_id='extract_user',
        http_conn_id='user_api',  # Connection ID for the API
        endpoint='api/',  # API endpoint for data extraction
        method='GET',  # HTTP GET method
        response_filter=lambda response: json.loads(response.text),  # Parse JSON response
        log_response=True  # Log the API response
    )

    # Task to process the extracted user data
    process_user = PythonOperator(
        task_id='process_user',
        python_callable=_process_user  # Call the processing function
    )

    # Task to store the processed user data in the Postgres database
    store_user = PythonOperator(
        task_id='store_user',
        python_callable=_store_user  # Call the storage function
    )

    # Define task dependencies
    create_table >> is_api_available >> extract_user >> process_user >> store_user
