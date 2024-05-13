from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes de la llamada de la funcion")
        result=func(*args,**kwargs)
        print("Despues de llamar a la funcion")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Funcion para saludar a alguien"""
    return (f"Hola, {name}").upper()

print(greet("Juan"))
print("1")
print(greet.__name__)
print("2")
print(greet.__doc__)


