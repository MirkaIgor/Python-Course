"""
В файле `input.txt` будет содержаться текст, переверните каждое слово (непробельные символы) 
задом наперёд и запишите в этот же файл.

Вы можете открыть файл на чтение-и-запись, читать построчно и сразу же записывать обработанную 
строку на исходное место; для этого пригодятся функции `file.tell()` и `file.seek()` - чтения 
и установки текущего положения.

Или же сперва прочитать весь файл, обработать, и перезаписать.

пример ввода:
    meroL  muspI  -  отэ  ,"абыр"-тскет  отсач йымеузьлопси в итачеп и .енйазид-бэв
    meroL   muspI   ястеялвя   йонтраднатс   "йобыр"   ялд   вотскет   ан  ецинитал
    с алачан IVX .акев
    В  от  ямерв йикен йыннямызеб кинтачеп ладзос юушьлоб юицкеллок воремзар и мроф
    ,вотфирш яузьлопси meroL muspI ялд иктачепсар .воцзарбо

пример вывода:
    Lorem  Ipsum  -  это  текст-"рыба",  часто используемый в печати и вэб-дизайне.
    Lorem   Ipsum   является   стандартной   "рыбой"   для   текстов   на  латинице
    с начала XVI века.
    В  то  время некий безымянный печатник создал большую коллекцию размеров и форм
    шрифтов, используя Lorem Ipsum для распечатки образцов.
"""

FILENAME = 'hw-03/input.txt'

def invert_text(text: str):
    lines = text.split('\n')
    for ind_line,line in enumerate(lines):
        words = line.split(' ')
        for ind,word in enumerate(words):
            words[ind] = word[::-1]
        lines[ind_line] = ' '.join(words)
    return '\n'.join(lines)

with open(FILENAME,'r+',encoding='utf-8') as file:
    text = invert_text(file.read())
    file.seek(0)
    file.write(text)

#======= Previous decision =========
# file = open('hw-03/input.txt','r',encoding='utf-8')
# text = invert_text(file.read())
# file.close()
# file = open('hw-03/input.txt','w',encoding='utf-8')
# file.write(text)
# file.close()


