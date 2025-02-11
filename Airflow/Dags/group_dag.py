from airflow import DAG
from airflow.operators.bash import BashOperator
from groups.group_downloads import download_tasks
from groups.group_transforms import transforms_tasks
from datetime import datetime

# Define the DAG
with DAG(
    'group_dag',  # Unique name for the DAG
    start_date=datetime(2022, 1, 1),  # Scheduling begins from this date
    schedule_interval='@daily',  # Run daily
    catchup=False  # Skip any backfilling of missed runs
) as dag:

    # Create a dictionary with DAG parameters (optional, for consistency)
    args = {'start_date': dag.start_date, 'schedule_interval': dag.schedule_interval, 'catchup': dag.catchup}

    # Group tasks for downloads, imported from the `group_downloads` module
    downloads = download_tasks()

    # Task to check files after downloads are completed
    check_files = BashOperator(
        task_id='check_files',  # Unique task ID
        bash_command='sleep 10'  # Simulated check with a delay
    )

    # Group tasks for transformations, imported from the `group_transforms` module
    transforms = transforms_tasks()

    # Set task dependencies: downloads -> check_files -> transforms
    downloads >> check_files >> transforms
