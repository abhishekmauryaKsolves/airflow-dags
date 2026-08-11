from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def github_test():
    print("🔥 GitHub → GitDagBundle → Airflow is working!")


with DAG(
    dag_id="github_auto_sync_test",
    start_date=datetime(2026, 8, 11),
    schedule=None,
    catchup=False,
    tags=["github", "gitdagbundle", "test"],
) as dag:

    test_task = PythonOperator(
        task_id="github_bundle_test",
        python_callable=github_test,
    )
