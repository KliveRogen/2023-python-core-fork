import time


def time_log(input_func):
    def output_func(*args, **kwargs):
        start_time = time.time()
        print(f"[{get_formatted_time()}] Старт метода {input_func.__qualname__}")
        result = input_func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"[{get_formatted_time()}] Метод {input_func.__qualname__} выполнен за {execution_time} секунд")
        return result

    return output_func


def get_formatted_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")
