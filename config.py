import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="soap_db",
        user='postgres',
        password='1234')
