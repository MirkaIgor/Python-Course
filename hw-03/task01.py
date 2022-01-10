"""Определите классы исключений PreconditionError и ComplexRootError и напишите функцию solve(a, b, c), которая:
принимает целые или вещественные коэффициенты (в противном случае возбуждает ошибку TypeError)
проверяет предусловие a!=0 (в противном случае возбужает PreconditionError)
решает уравнение с вещественными корнями (в противном случае возбуждает ComplexRootError)
возвращает кортеж из 1 или 2 корней, упорядоченных по возрастанию
исключения должны содержать информацию о том, какие аргументы привели к ошибке.
пример ввода:
  1 2 1
  0.25 -2.5 6
  1 0 1
  0 1 -2
  1j 2 3
  1 "2" "3"
пример вывода:
  -1.0
  4.0 6.0
  Исключение: комплексные корни с аргументами: 1, 0, 1
  Исключение: нарушение предусловия a!=0
  Исключение: неправильные типы: 1 аргумент
  Исключение: неправильные типы: 2, 3 аргументы"""

from math import sqrt

class PreconditionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Исключение: нарушение предусловия a!=0",*args)

class ComplexRootError(Exception):
    def __init__(self, a, b, c, *args: object) -> None:
        super().__init__(f'Исключение: комплексные корни с аргументами: {a}, {b}, {c}',*args)

def solve(a,b,c):
    """Function solves quadratic equation of the form ax^2+bx+c=0"""
    error_argument = [False,False,False]
    args = (a,b,c)
    for ind,val in enumerate(args):
        if not isinstance(val,(int,float)):
            error_argument[ind]=True

    if error_argument.count(True) == 1:
        arg_message = str(error_argument.index(True)+1) + ' аргумент'
        raise TypeError(f'Исключение: неправильные типы: {arg_message}')
    elif error_argument.count(True) > 1:
        arg_message = ', '.join([str(i+1) for i, x in enumerate(error_argument) if x == True])+' аргументы'
        raise TypeError(f'Исключение: неправильные типы: {arg_message}')

    if a==0:
        raise PreconditionError()

    discr = b**2-4*a*c

    if discr < 0:
        raise ComplexRootError(a,b,c)

    if discr == 0:
        return str(-b/(2*a))
    else:
        x = [(-b+sqrt(discr))/(2*a),(-b - sqrt(discr))/(2*a)]
        x.sort()
        x = [str(i) for i in x]
        return ', '.join(x)

if __name__ == '__main__':
    actions = (lambda: solve(1,2,1),
            lambda: solve(0.25,-2.5,6),
            lambda: solve(1,0,1),
            lambda: solve(0,1,-2),
            lambda: solve(1j,2,3),
            lambda: solve(1,"2","3"))
    for act in actions:
        try:
            print(act())
        except Exception as err:
            print(err)