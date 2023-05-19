import time

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        func(*args)
        end=time.time()
        print('Time elapsed ',end-start)
    return wrapper
