import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user='postgres',
        password='1234')