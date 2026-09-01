from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def demo_task():
    print("GitHub DAG successfully deployed through MinIO")


with DAG(
    dag_id="github_to_minio_demo",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
) as dag:

    test = PythonOperator(
        task_id="test_github_to_minio",
        python_callable=demo_task,
    )
