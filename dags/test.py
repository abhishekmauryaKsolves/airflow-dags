from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def test():
    print("Hello Client! DAG deployed from GitHub to Airflow via MinIO")

with DAG(
    dag_id="client_demo_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["demo"],
) as dag:

    hello_task = PythonOperator(
        task_id="test",
        python_callable=hello_client
    )
