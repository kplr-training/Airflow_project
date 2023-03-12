"""Simple dag #2."""
from airflow import models
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import python_operator
from airflow.utils.dates import days_ago


with models.DAG(
        'dag_2',
        schedule_interval='*/1 * * * *',  # Every 1 minute
        start_date=days_ago(0),
        catchup=False) as dag:
    def greeting():
        """Just check that the DAG is started in the log."""
        import logging
        logging.info('Hello World from DAG 2')

    hello_python = python_operator.PythonOperator(
        task_id='hello',
        python_callable=greeting)

    goodbye_dummy = DummyOperator(task_id='goodbye')

    hello_python >> goodbye_dummy