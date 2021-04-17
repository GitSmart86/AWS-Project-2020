# FROM python:3.8.3-buster
# COPY . /app
# WORKDIR /app
# RUN pip3 install -r requirements.txt
# CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000


# Code Source from cps420/tools/kubernetes


FROM python:3.8.3

RUN apt-get update && apt-get install -y postgresql-client

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD echo "SELECT 'CREATE DATABASE $DBNAME' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$DBNAME')\gexec" | PGPASSWORD=$PGPASS psql -h $DBHOST && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000