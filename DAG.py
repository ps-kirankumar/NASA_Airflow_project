from datetime import timedelta  # Import timedelta for defining time intervals
from airflow import DAG  # Import DAG class from Airflow
from airflow.operators.python import PythonOperator  # Import PythonOperator for executing Python functions
from datetime import datetime  # Import datetime module for working with dates and times
from Access_nasa import fetch_neo_data  # Import the function fetch_neo_data from Access_nasa module

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',  # Owner of the DAG
    'depends_on_past': False,  # DAG does not depend on past executions
    'start_date': datetime(2024, 1, 31),  # Start date of DAG execution
    'email': ['airflow@example.com'],  # Email address for DAG notifications
    'email_on_failure': False,  # Disable email notifications on failure
    'email_on_retry': False,  # Disable email notifications on retry
    'retries': 1,  # Number of retries for failed tasks
    'retry_delay': timedelta(minutes=1)  # Delay between retries
}

# Define the DAG object
dag = DAG(
    'neo_dag',  # DAG ID
    default_args=default_args,  # Default arguments for the DAG
    description='My first DAG with ETL process!',  # Description of the DAG
    schedule_interval=timedelta(days=1),  # Interval between DAG runs
)

# Define a PythonOperator task to execute the fetch_neo_data function
run_etl = PythonOperator(
    task_id='complete_nasa_etl',  # Task ID
    python_callable=fetch_neo_data,  # Python function to execute
    dag=dag,  # Assign the task to the defined DAG
)

run_etl  # Return the PythonOperator task
