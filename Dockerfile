FROM python:3.8.3

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y cron postgresql-client
RUN pip3 install -r requirements.txt

COPY pulsar-cron /etc/cron.d/pulsar-cron
RUN chmod 0644 /etc/cron.d/pulsar-cron
RUN crontab /etc/cron.d/pulsar-cron
RUN touch /var/log/cron.log

CMD cron && chmod +x cron.sh && ./cron.sh && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000 && python3 manage.py load_data && python3 manage.py process_pulsar

# CMD echo "SELECT 'CREATE DATABASE $DBNAME' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$DBNAME')\gexec" | PGPASSWORD=$PGPASS psql -h $DBHOST 
# && python3 manage.py migrate 
# && python3 ./atc/pop_database.py 
# && python3 manage.py runserver 0.0.0.0:8000
