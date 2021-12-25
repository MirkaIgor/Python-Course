def gen_str_numbers(number: int):

    prefixes = {0:'',1:'один',2:'дв',3:'три',4:'четыр',5:'пят',6:'шест',7:'сем',8:'восем',
                9:'девят',10:'десят'}

    prefixes_end = {0:'ноль',1:'',2:'а',3:'',4:'е',5:'ь',6:'ь',7:'ь',8:'ь',
                        9:'ь',10:'ь'}
    
    suffixes = {10:'надцать',20:'двадцать',30:'тридцать',40:'сорок',90:'девяносто'}
    for i in range(50,90,10):
        suffixes.update({i:prefixes[i/10]+prefixes_end[i/10]+prefixes[10]})

    if number in range(0,11):
        return prefixes[number]+prefixes_end[number]
    elif number in range(11,20):
        if number == 12:
            return prefixes[2]+'e'+suffixes[10]
        return prefixes[number%10]+suffixes[10]
    elif number in range(20,100):
        j = number%10
        i = number-j
        if j == 0:
            return suffixes[i]+prefixes[j]
        return suffixes[i]+' '+prefixes[j]+prefixes_end[j]
    else:
        return "Error: Entered number not in 0-99"


if __name__ == '__main__':
    print('For exit press Ctrl+C')
    while True:
        print('Вывод: ',gen_str_numbers(int(input('Ввод: '))))

    
