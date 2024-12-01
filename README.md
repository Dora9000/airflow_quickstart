# Apache Airflow 2.0

Создаём виртуальное окружение и активируем его:

```
python3 -m venv .venv
source .venv/bin/activate
```

Обновляем версию пакетного менеджера pip:
```
pip install pip -U
```

Устанавливаем Airflow (python 3.8):
```
pip install apache-airflow[postgres,aws]==2.0.1 --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.8.txt
```
https://startdatajourney.com/ru/course/apache-airflow-2/modules/9/25/1


Настраиваем переменные окружения (редактируемое):
```
export AIRFLOW_HOME=~/airflow-data
```

Инициализируруем БД:
```
airflow db init
```

Поднимаем контейнер с postgres:
```
docker run -d -p 6666:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_USER=airflow -e POSTGRES_DB=airflow -v postgres_data_airflow:/var/lib/postgresql/data postgres:13.1

```

Настраиваем коннекшн к postgres (в airflow.cfg):
```
executor = LocalExecutor
sql_alchemy_conn = postgresql+psycopg2://airflow:password@localhost:6666/airflow
load_examples = False
dags_folder = ...(путь, где лежат DAG)
```


Переинициализируруем БД:
```
airflow db init

(airflow db reset)
```


Авторизация в Airflow:
```
airflow users create \
    --username airflow \
    --firstname Airflow \
    --lastname Apache \
    --role Admin \
    --email airflow@example.com \
    --password airflow
```


Запуск сервера:
```
airflow webserver -p 8080
```

Запуск скедулера:
```
airflow scheduler
```


