import datetime

from airflow.models import DAG
from airflow.operators.python import PythonOperator, get_current_context
from airflow.operators.dummy import DummyOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2024, 11, 20),
}


def even_only():
    context = get_current_context()
    execution_date = context['execution_date']

    if execution_date.day % 2 != 0:
        raise ValueError(f'Odd day: {execution_date}')


with DAG(dag_id='dag_with_two_tasks',
         schedule_interval='@daily',
         default_args=default_args) as dag:

    even_only = PythonOperator(
        task_id='even_only',
        python_callable=even_only,
        dag=dag,
    )

    dummy = DummyOperator(
        task_id='dummy_task',
        dag=dag
    )

    even_only >> dummy

    # другие варианты:

    # dummy.set_upstream(even_only)
    # even_only.set_downstream(dummy)
    # dummy << even_only