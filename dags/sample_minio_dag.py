from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def print_status():
    print("Airflow + MinIO pipeline is working correctly!")


default_args = {
    "owner": "abhishek",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="sample_minio_pipeline",
    default_args=default_args,
    description="A sample DAG for MinIO-based deployment testing",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["minio", "sample", "deployment"],
) as dag:

    start = EmptyOperator(task_id="start")

    check_system = PythonOperator(
        task_id="check_system",
        python_callable=print_status,
    )

    end = EmptyOperator(task_id="end")

    start >> check_system >> end
