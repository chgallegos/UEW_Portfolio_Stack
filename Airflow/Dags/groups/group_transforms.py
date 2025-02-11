from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

# Define a function to group transformation tasks
def transforms_tasks():
    # Create a TaskGroup for organizing transformation tasks
    with TaskGroup("transforms", tooltip="Transform tasks") as group:
        
        # Task to simulate transforming data A
        transform_a = BashOperator(
            task_id='transform_a',  # Unique ID for the task
            bash_command='sleep 10'  # Simulates a transformation with a 10-second delay
        )
    
        # Task to simulate transforming data B
        transform_b = BashOperator(
            task_id='transform_b', 
            bash_command='sleep 10'
        )
    
        # Task to simulate transforming data C
        transform_c = BashOperator(
            task_id='transform_c', 
            bash_command='sleep 10'
        )

        # Return the task group
        return group
