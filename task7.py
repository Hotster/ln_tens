from datetime import datetime

def func_time(func):
    time_now = datetime.now()
    func()
    f_time = datetime.now() - time_now
    return f'Функция {func.__name__} выполнялась {datetime.strftime(f_time, "%S")} секунд'


@func_time
def some_func():
    for i in range(0, 100000000):
        pass


print(some_func)
