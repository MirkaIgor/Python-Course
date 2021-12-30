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
    pass

class ComplexRootError(Exception):
    pass

def solve(a,b,c):
    """Function solves quadratic equation of the form ax^2+bx+c=0"""
    try:
        if a==0:
            raise PreconditionError("Исключение: нарушение предусловия a!=0")

        discr = b**2-4*a*c

        if discr < 0:
            raise ComplexRootError("Исключение: комплексные корни с аргументами: {0}, {1}, {2}".format(a,b,c))
    except TypeError:
        error_argument = [False,False,False]
        if not isinstance(a,(int,float)):
            error_argument[0]=True
        if not isinstance(b,(int,float)):
            error_argument[1]=True
        if not isinstance(c,(int,float)):
            error_argument[2]=True
        if error_argument.count(True) == 1:
            arg_message = str(error_argument.index(True)+1) + ' аргумент'
        else:
            arg_message = ', '.join([str(i+1) for i, x in enumerate(error_argument) if x == True])+' аргументы'
        err_msg = "Исключение: неправильные типы: " + arg_message
        return err_msg
    except PreconditionError as err:
        return err.args[0]
    except ComplexRootError as err:
        return err.args[0]

    if discr == 0:
        return str(-b/(2*a))
    else:
        x = [(-b+sqrt(discr))/(2*a),(-b - sqrt(discr))/(2*a)]
        x.sort()
        x = [str(i) for i in x]
        return ', '.join(x)

if __name__ == '__main__':
    print(solve(1,2,1))
    print(solve(0.25,-2.5,6))
    print(solve(1,0,1))
    print(solve(0,1,-2))
    print(solve(1j,2,3))
    print(solve(1,"2","3"))