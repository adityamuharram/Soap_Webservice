import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="mahasiswa",
        user='postgres',
        password='1234')
