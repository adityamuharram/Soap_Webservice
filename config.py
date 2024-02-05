import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="db_mahasiswa",
        user='pi',
        password='1234')
