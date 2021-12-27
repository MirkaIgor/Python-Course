def count_sum_mul_pow(a,b):
    return (a+b,a*b,a**b)

print("Ввод:")
a = int(input())
b = int(input())
res = count_sum_mul_pow(a,b)
print('Вывод:\n',res[0],res[1],res[2])
