from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

# Define a dataset that tracks updates to a file
my_file = Dataset("/tmp/my_file.txt")

# Define the DAG that reacts to changes in the dataset
with DAG(
    dag_id="consumer",
    schedule=[my_file],  # Run the DAG when the dataset is updated
    start_date=datetime(2022, 1, 1),  # Schedule starts on this date
    catchup=False  # Skip missed runs since the start_date
):
    
    @task
    def read_dataset():
        # Open and read the file referenced by the dataset
        with open(my_file.uri, "r") as f:
            print(f.read())  # Print the file's content

    # Call the task within the DAG
    read_dataset()
