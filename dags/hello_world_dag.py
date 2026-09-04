from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def hello_world():
    print("Hello World i am there")


with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
) as dag:

    hello = PythonOperator(
        task_id="hello_world",
        python_callable=hello_world,
    )
