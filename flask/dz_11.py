from contextlib import contextmanager
from time import time as tm


class Lock(object):
    def __init__(self):
        self.lock = False

    def __enter__(self, *args, **kwargs):
        self.lock = True

    def __exit__(self, *args, **kwargs):
        print(self.lock)


with Lock() as f:
    pass


def some_long_function():
    return 1000 ** 100 / 1000000**5879


class TimeIt:

    def __enter__(self, *args):
        self.stime = tm()
        return self

    def __exit__(self, *args):
        self.etime = tm()
        self.time = self.etime - self.stime


with TimeIt() as t:
    some_long_function()
    print('Execution time was:', t.time)

@contextmanager
def no_exception():
    try:
        yield
    except Exception as e:
        print(e)


with no_exception():
    1/0