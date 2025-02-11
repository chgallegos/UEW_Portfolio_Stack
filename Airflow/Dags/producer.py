from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

# Define a dataset to track updates
my_file = Dataset("/tmp/my_file.txt")

# Define the DAG
with DAG(
    dag_id="producer",  # Unique identifier for the DAG
    schedule="@daily",  # Run the DAG daily
    start_date=datetime(2022, 1, 1),  # Start scheduling from this date
    catchup=False  # Do not run for past dates
):
    
    # Define a task that writes to the dataset
    @task(outlets=[my_file])  # Declare my_file as the output of this task
    def update_dataset():
        with open(my_file.uri, "a") as f:  # Open the file in append mode
            f.write("producer update")  # Write a message to the file
    
    # Add the task to the DAG
    update_dataset()
