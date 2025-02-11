from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

# Function for Task t1: Pushes a value (42) into XCom
def _t1(ti):
    ti.xcom_push(key='my_key', value=42)

# Function for Task t2: Pulls the value from XCom (set by t1)
def _t2(ti):
    ti.xcom_pull(key='my_key', task_ids='t1')

# Function for branching: Determines which task to follow based on XCom value
def _branch(ti):
    value = ti.xcom_pull(key='my_key', task_ids='t1')  # Pull value from t1
    if value == 42:  # If value is 42, proceed to t2
        return 't2'
    return 't3'  # Otherwise, proceed to t3

# Define the DAG
with DAG(
    "xcom_dag",  # Unique identifier for the DAG
    start_date=datetime(2022, 1, 1),  # Scheduling begins from this date
    schedule_interval='@daily',  # Run the DAG daily
    catchup=False  # Skip backfilling for past dates
) as dag:
    
    # Task t1: Push a value (42) into XCom
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )

    # Task branch: Decides whether to execute t2 or t3
    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=_branch
    )
    
    # Task t2: Pulls and processes the XCom value from t1
    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )
    
    # Task t3: Executes a Bash command as an alternative branch
    t3 = BashOperator(
        task_id='t3',
        bash_command="echo ''"  # Placeholder command
    )

    # Task t4: Executes after either t2 or t3, regardless of which branch succeeded
    t4 = BashOperator(
        task_id='t4',
        bash_command="echo ''",  # Placeholder command
        trigger_rule='one_success'  # Executes if at least one upstream task succeeds
    )

    # Define task dependencies
    t1 >> branch >> [t2, t3] >> t4
