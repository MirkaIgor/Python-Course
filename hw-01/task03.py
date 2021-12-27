def gen_str_numbers(number: int):

    nums0_10 = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',
                9:'девять',10:'десять'}

    nums11_19 = {11:'одиннадцать',12:'двенадцать',13:'тринадцать',14:'четырнадцать',15:'пятнадцать',
                16:'шестнадцать',17:'семнадцать',18:'восемнадцать',19:'двадцать'}

    krat10nums = {20:'двадцать',30:'тридцать',40:'сорок',50:'пятьдесят',60:'шестьдесят',
                70:'семьдесят',80:'восемдесят',90:'девяносто'}

    if number >= 0 and number < 11:
        return nums0_10[number]

    elif number >= 11 and number < 20:
        return nums11_19[number]

    elif number >= 20 and number < 100:
        j = number%10
        i = number-j
        if j == 0:
            return krat10nums[number]
        else:
            return krat10nums[i]+' '+nums0_10[j]
    else:
        return "Error: Entered number not in 0-99"


if __name__ == '__main__':
    print("For exit type 'q' in input")
    while True:
        inp = input('Ввод: ')
        if inp == 'q':
            break
        print('Вывод: ',gen_str_numbers(int(inp)))

    
