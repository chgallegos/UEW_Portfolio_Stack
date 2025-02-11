from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

# Define a function to group download tasks
def download_tasks():
    # Create a TaskGroup for organizing download tasks
    with TaskGroup("downloads", tooltip="Download tasks") as group:    
        
        # Task to simulate downloading file A
        download_a = BashOperator(
            task_id='download_a',  # Unique ID for the task
            bash_command='sleep 10'  # Simulates a download with a 10-second delay
        )
        
        # Task to simulate downloading file B
        download_b = BashOperator(
            task_id='download_b', 
            bash_command='sleep 10'
        )
        
        # Task to simulate downloading file C
        download_c = BashOperator(
            task_id='download_c', 
            bash_command='sleep 10'
        )

        # Return the task group
        return group
