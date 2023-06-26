from functools import wraps
import tracemalloc
from time import perf_counter 
import datetime


def mem_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def profile(func):
    '''Measure performance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        total_time = finish_time - start_time
        total_time = datetime.timedelta(seconds=total_time)

        print(f'{"="*40}')
        print("---- Meta Data ----")
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print("---- Memory Usage ----")
        print(f'Current memory usage:\t {mem_fmt(current)}\n'
              f'Peak memory usage:\t {mem_fmt(peak)}')
        print("---- Time ----")
        print(f'Total Time:\t {total_time}\n'
              f'seconds:\t {total_time.seconds}\n'
              f'microseconds:\t {total_time.microseconds}')
        print(f'{"="*40}')
        tracemalloc.stop()
    return wrapper