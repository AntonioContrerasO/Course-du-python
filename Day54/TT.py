import time


def delay(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay
def hello():
    print("Hello")

@delay
def bye():
    print("Bye")

hello()