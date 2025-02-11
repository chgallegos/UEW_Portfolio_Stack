from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

# Define datasets that will trigger the DAG when updated
my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

# Define the DAG
with DAG(
    dag_id="multiple_consumer",  # Unique identifier for the DAG
    schedule=[my_file, my_file_2],  # Trigger the DAG when either dataset is updated
    start_date=datetime(2022, 1, 1),  # Start scheduling from this date
    catchup=False  # Disable backfilling of missed runs
):
    
    # Define a task to read the first dataset
    @task
    def read_dataset():
        with open(my_file.uri, "r") as f:  # Open the file specified in my_file
            print(f.read())  # Print the content of the file to logs

    # Add the task to the DAG
    read_dataset()
