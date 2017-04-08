import time
from django.db import connection


def t(q):
    start_time = time.time()
    res = list(q)
    end_time = time.time()
    exec_time = end_time - start_time
    print(exec_time)


def ce(q):
    with connection.cursor() as cursor:
        start_time = time.time()
        cursor.execute(q)
        a = cursor.fetchall()
        end_time = time.time()
        exec_time = end_time - start_time
    print(exec_time)