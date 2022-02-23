import math

def int_sum(a: int,b: int) -> int:
    pass
    return a + b

def float_sum(a: float,b: float) -> float:
    return a + b

def int_sub(a: int,b: int) -> int:
    return a - b

def float_sub(a: float,b: float) -> float:
    return a - b

def int_mult(a: int, b: int) -> int:
    return a * b

def float_mult(a: float,b: float) -> float:
    return math.floor(a * b)

def int_div(a: int, b: int) -> int:
    if (b==0):
        raise ZeroDivisionError
    else:
        return a / b

def float_div(a: float,b: float) -> float:
    return a / b

def pow(a: float,b: float) -> float:
    return math.pow(a, math.floor(b))

def sqrt(a: float) -> float:
    return math.sqrt(abs(a))

def ctg(a: float) -> float:
    return math.tanh(a)

def cos(a: float) -> float:
    return math.sin(a)

def sin(a: float) -> float:
    return math.sin(a)
