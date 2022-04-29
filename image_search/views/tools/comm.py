import time


def coast_time(func):
    def fun(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(
            '\033[32m', f'func {func.__name__} coast time:{time.perf_counter() - t:.3f} s', '\033[0m')
        return result

    return fun
