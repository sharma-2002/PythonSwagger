import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Replace these variables with your database details
db_name = "offline_db"
db_user = "sphati_admin"
db_password = "r@gnar0k"
db_host = "3.110.153.217"
db_port = "5432"
connection = create_connection(db_name, db_user, db_password, db_host, db_port)