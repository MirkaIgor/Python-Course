"""
Программа будет получать на вход аргументы из командной строки

Аргументы командной строки – коэффициенты и переменная полинома:

P(x)=an⋅xn+an−1⋅xn−1+...+a1⋅x+a0 (ПРОВЕРЬ В HTML. Там степени)
 
-a                  - коэффициенты ai (float, от старшего к младшему)
-x VALUE            – величина x (float)
-v или --verbose    – выводит вычисляемое выражение "an*xn+...+a1*x+a0*1.0=p", где
                      ai - коэффициенты
                      xi - вычисленная i-я степень числа x
                      p - итоговое значение

если флаг verbose отсутствует, то скрипт просто выводит итоговое значение.


примеры ввода:
    ./script.py -a 1 2 3 -x 0
    ./script.py -a 1 2 3 -x 2 --verbose

приверы вывода:
    3.0
    1.0*4.0+2.0*2.0+3.0*1.0=11.0


для разбора аргументов применяйте пакет argparse (https://docs.python.org/3/howto/argparse.html)

ПРИМЕР ИСПОЛЬЗОВАНИЯ:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-q', '--question', action='store_true')
    parser.add_argument('-x', nargs='?', const=777, default=888, type=int)
    parser.add_argument('-y', nargs='?', const=111, default=222)
    parser.add_argument('-z', nargs='?', const=333, default=444)
    parser.add_argument('rest', nargs='...')

    ns = parser.parse_args('-x -z alfa hello.txt beta gamma delta'.split())
    # ns.file = 'hello.txt'
    # ns.question = False
    # ns.x = 777
    # ns.y = 222
    # ns.z = 'alfa'
    # ns.rest = ['beta', 'gamma', 'delta']

    sys.argv = 'script.py -x -z alfa hello.txt beta gamma delta'.split()
    ns = parser.parse_args()  # тот же эффект`
"""
import argparse

def count_polynome(a: list, x: float, verbose: bool):
    a_inv = a[::-1]
    x = x[0]
    max_koef = len(a)-1
    result=None

    cur_res = 0
    for i in range(max_koef,-1,-1):
        cur_res+=a_inv[i]*(x**i)
    result = cur_res
    
    my_str=''
    if verbose:
        my_str+='Вычислено:\n'
        for i in range(max_koef,-1,-1):
            my_str += '{0}*{1}+'.format(str(a_inv[i]),str(x**i))
        return my_str[:-1]+'='+str(result)
    else:
        return 'Вычислено:\n'+str(result)
        
parser = argparse.ArgumentParser()
parser.add_argument('-a',nargs='+',required=True,type=float,help='коэффициенты ai (float, от старшего к младшему)')
parser.add_argument('-x',nargs=1,required=True,type=float,help='величина x (float)')
parser.add_argument('-v','--verbose',action='store_true',help="выводит вычисляемое выражение \"an*xn+...+a1*x+a0*1.0=p\", где\
                                                            ai - коэффициенты\
                                                            xi - вычисленная i-я степень числа x\
                                                            p - итоговое значение")

if __name__ == '__main__':
    my_args = parser.parse_args('-a 1 2 3 -x 0'.split())
    print(count_polynome(my_args.a,my_args.x,my_args.verbose))
    my_args = parser.parse_args('-a 1 2 3 -x 2 -v'.split())
    print(count_polynome(my_args.a,my_args.x,my_args.verbose))
