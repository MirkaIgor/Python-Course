#Task1 Homework2

def sum_text_numbers(a:str,b:str):
    """Method counts sum of two digits entered by Russian name."""
    number_lib = {'ноль':0,'один':1,'два':2,'три':3,'четыре':4,
                'пять':5,'шесть':6,'семь':7,'восемь':8,'девять':9}

    ans_num_list = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь',
                'девять','десять','одиннадцать','двенадцать','тринадцать','четырнадцать',
                'пятнадцать','шестнадцать','семнадцать','восемнадцать']

    try:
        a = number_lib[a]
        b = number_lib[b]
    except KeyError:
        return "Error: Not valid values. Parameters 'a' and 'b' must be digit 0-9 by Russian name"

    return ans_num_list[a+b]

if __name__ == '__main__':
    print("For exit type 'q' in input")
    while True:
        print("Ввод:")
        a = input()
        b = input()
        if a == 'q' or b == 'q':
            break
        print('Вывод:\n',sum_text_numbers(a,b))