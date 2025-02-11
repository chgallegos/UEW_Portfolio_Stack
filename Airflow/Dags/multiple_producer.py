from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

# Define datasets to track and trigger downstream DAGs
my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

# Define the DAG
with DAG(
    dag_id="multiple_producer",  # Unique identifier for the DAG
    schedule="@daily",  # Run the DAG daily
    start_date=datetime(2022, 1, 1),  # Start scheduling from this date
    catchup=False  # Skip missed runs prior to start_date
):
    
    # Task to update the first dataset
    @task(outlets=[my_file])  # Declare my_file as the output dataset
    def update_dataset():
        with open(my_file.uri, "a") as f:  # Open the file in append mode
            f.write("producer update 1")  # Write a message to the file

    # Task to update the second dataset
    @task(outlets=[my_file_2])  # Declare my_file_2 as the output dataset
    def update_dataset_2():
        with open(my_file_2.uri, "a") as f:  # Open the file in append mode
            f.write("producer update 2")  # Write a message to the file

    # Define the task execution order: update_dataset -> update_dataset_2
    update_dataset() >> update_dataset_2()
