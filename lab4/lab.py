import requests
import time

def rate_limiter(interval):
    def decorator(func):
        last_called = [0]
        def wrapper():
            current_time = time.time()
            if current_time - last_called[0] < interval:
                return "Превышена частота вызовов."
            last_called[0] = current_time
            return func()
        return wrapper
    return decorator

def outers(zov):
    @rate_limiter(5)
    def closure():
        z = requests.get(zov)
        return z.text
    return closure

answer = outers("https://dogapi.dog/api/v2/facts")

print(answer())
print(answer())
time.sleep(5)
print(answer())