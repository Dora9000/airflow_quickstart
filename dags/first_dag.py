import random
import datetime

from airflow.models import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2024, 11, 20),
    'retries': 2,
    'retry_delay': datetime.timedelta(seconds=10),
}


def random_dice():
    val = random.randint(1, 6)
    if val % 2 != 0:
        raise ValueError(f'Odd {val}')


with DAG(dag_id='first_dag',
         schedule_interval='@daily',
         default_args=default_args) as dag:

    dice = PythonOperator(
        task_id='random_dice',
        python_callable=random_dice,
        dag=dag,
    )
