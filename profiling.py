from django.db import connection
from cProfile import Profile
from pyprof2calltree import convert
from httc.models import Order as HttcOrder


def cursor_execute_profiler():
    cursor = connection.cursor()
    profiler = Profile()
    for _ in range(10):
        profiler.runctx(
            "cursor.execute('''SELECT * FROM httc_order WHERE mk_contract_id = 1000 ORDER BY price''')",
            locals(), globals())
    convert(profiler.getstats(), 'cursor_execute_profiler.kgrind')


def raw_sql_profiler():
    profiler = Profile()
    for _ in range(10):
        profiler.runctx(
            "list(HttcOrder.objects.raw('''SELECT * FROM httc_order WHERE mk_contract_id = 1000 ORDER BY price'''))",
            locals(), globals())
    convert(profiler.getstats(), 'raw_sql_profiler.kgrind')
