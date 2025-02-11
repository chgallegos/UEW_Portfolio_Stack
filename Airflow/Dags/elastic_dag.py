from airflow import DAG
from airflow.operators.python import PythonOperator
from hooks.elastic.elastic_hook import ElasticHook
from datetime import datetime

# Define a function to interact with Elasticsearch and print its info
def _print_es_info():
    hook = ElasticHook()  # Create an instance of the custom ElasticHook
    print(hook.info())  # Fetch and print Elasticsearch cluster info

# Define the DAG
with DAG(
    'elastic_dag',  # Unique ID for the DAG
    start_date=datetime(2022, 1, 1),  # Start scheduling from this date
    schedule_interval='@daily',  # Run daily
    catchup=False  # Do not run for past dates
) as dag:
    
    # Define a task that executes the _print_es_info function
    print_es_info = PythonOperator(
        task_id='print_es_info',  # Unique ID for the task
        python_callable=_print_es_info  # Reference to the Python function
    )
