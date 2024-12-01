import datetime as dt
import asyncio
from airflow.decorators import dag, task
from airflow.operators.python import get_current_context
from airflow.operators.dummy import DummyOperator
import logging


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2024, 11, 1),
}


async def async_task2():
    logging.info('Hello from async_task2')
    return {"is_ok": True}

@dag(
    default_args=default_args,
    schedule_interval='@daily',
    dag_id='async_dag_3',
    # catchup=False,
)
def async_dag():
    @task
    def task1():
        logging.info('Hello from task1')


    @task
    def task2():
        result = asyncio.run(async_task2())

        logging.info('Hello from task2: ' + str(result))

    task1() >> task2()


main_dag = async_dag()
