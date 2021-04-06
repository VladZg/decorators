import time

PASSWORD = 'abcd'
n_print = print


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        n_print('Время выполнения: {}'.format(end - start))

    return wrapper


def check_password(func):
    def wrapper(*args, **kwargs):
        password = input('Введите пароль для получения доступа: ')
        if password == PASSWORD:
            func(*args, **kwargs)
        else:
            n_print('В доступе отказано')
            return None

    return wrapper


@check_password
@benchmark
def print(s):
    n_print(s.upper())


a = input()
print(a)
