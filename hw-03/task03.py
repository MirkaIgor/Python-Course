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

class Polynome:
    def __init__(self,a: list,x: float, verbose: bool) -> None:
        self.a = a
        self.a_inv = a[::-1]
        self.x = x[0]
        self.v = verbose
        self.max_koef = len(a)-1
        self.result=None
    
    def count(self):
        cur_res = 0
        for i in range(self.max_koef,-1,-1):
            cur_res+=self.a_inv[i]*(self.x**i)
        self.result = cur_res
        return cur_res

    def __str__(self) -> str:
        my_str=''
        if self.result:
            if self.v:
                my_str+='Вычислено:\n'
                for i in range(self.max_koef,-1,-1):
                    my_str += '{0}*{1}+'.format(str(self.a_inv[i]),str(self.x**i))
                return my_str[:-1]+'='+str(self.result)
            else:
                return 'Вычислено:\n'+str(self.result)
        else:
            my_str+= 'Выражение полинома:\n'
            for i in range(self.max_koef,0,-1):
                my_str+= '{0}*(x^{1})+'.format(str(self.a_inv[i]),str(i))
            my_str+= str(self.a_inv[0])+'=P(x)'
            return my_str
            


parser = argparse.ArgumentParser()
parser.add_argument('-a',nargs='+',required=True,type=float,help='коэффициенты ai (float, от старшего к младшему)')
parser.add_argument('-x',nargs=1,required=True,type=float,help='величина x (float)')
parser.add_argument('-v','--verbose',action='store_true',help="выводит вычисляемое выражение \"an*xn+...+a1*x+a0*1.0=p\", где\
                                                            ai - коэффициенты\
                                                            xi - вычисленная i-я степень числа x\
                                                            p - итоговое значение")

def run(args):
    p = Polynome(args.a,args.x,args.verbose)
    print(p)
    p.count()
    print(p)
    print()

if __name__ == '__main__':
    try:
        my_args = parser.parse_args()
    except:
        my_args = parser.parse_args('-a 1 2 3 -x 0'.split())
        run(my_args)
        my_args = parser.parse_args('-a 1 2 3 -x 2 -v'.split())
        run(my_args)
