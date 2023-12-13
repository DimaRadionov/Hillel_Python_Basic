from datetime import datetime


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконана за {execution_time}")
        return result
    return wrapper


@timing_decorator
def example_function_1():
    for _ in range(1000000):
        pass


@timing_decorator
def example_function_2():
    for _ in range(500000):
        pass


example_function_1()
example_function_2()
