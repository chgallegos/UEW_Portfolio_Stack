from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the DAG
with DAG(
    'parallel_dag',  # Unique name for the DAG
    start_date=datetime(2022, 1, 1),  # Start scheduling from this date
    schedule_interval='@daily',  # Run the DAG daily
    catchup=False  # Skip any backfilling of missed runs
) as dag:
    
    # Task to simulate extracting data from source A
    extract_a = BashOperator(
        task_id='extract_a',  # Unique ID for the task
        bash_command='sleep 10'  # Simulate work with a 10-second delay
    )

    # Task to simulate extracting data from source B
    extract_b = BashOperator(
        task_id='extract_b', 
        bash_command='sleep 10'
    )

    # Task to simulate loading data from source A
    load_a = BashOperator(
        task_id='load_a', 
        bash_command='sleep 10'
    )

    # Task to simulate loading data from source B
    load_b = BashOperator(
        task_id='load_b', 
        bash_command='sleep 10'
    )

    # Task to transform data, requiring higher CPU resources
    transform = BashOperator(
        task_id='transform',
        queue='high_cpu',  # Assign the task to a queue for high-CPU workloads
        bash_command='sleep 30'  # Simulate work with a 30-second delay
    )

    # Define task dependencies
    extract_a >> load_a  # extract_a must finish before load_a starts
    extract_b >> load_b  # extract_b must finish before load_b starts
    [load_a, load_b] >> transform  # Both load_a and load_b must complete before transform starts
