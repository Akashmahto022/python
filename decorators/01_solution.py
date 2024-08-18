import time

def  timmer(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-startTime} time")
        return result
    return wrapper

@timmer
def example_function(n):
    time.sleep(n)
    
example_function(2)

