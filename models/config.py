DB_URL = "postgresql+psycopg2://username:zfW547MJ@192.168.100.194:5433/prvent"
#DB_URL = "postgresql+psycopg2://username:passwd!@localhost:5433/prvent"
DB_ECHO = False

#docker exec -i pg_container_name /bin/bash -c "PGPASSWORD=pg_password pg_dump --username pg_username database_name" > /desired/path/on/your/machine/dump.sql
#docker exec -i pg_container_name /bin/bash -c "PGPASSWORD=pg_password psql --username pg_username database_name" < /path/on/your/machine/dump.sql
