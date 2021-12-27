#Task1 Homework4 (Generete song text)

def make_song(song_lib: dict,common_string: str):
    """The function generates song "Курочка по зёрнышку" (Im Radio ist ein Kuken). 
    It takes just string with common text for each couplet
    and Dict of song filling"""

    song_list = list(song_lib.keys())
    song_text = ''
    for couplet in range(len(song_list)-1):
        song_text = song_text+'{0} {1}!\n{0} {1}!\n'.format(common_string,song_list[couplet])
        for string in range(couplet,-1,-1):
            song_text=song_text+'{0},\n'.format(song_lib[song_list[string]])
        song_text = song_text[:-2]+'.\n\n'
    song_text = song_text+'{0} {1}!\n{0} {1}!\n{2}'.format(common_string,song_list[-1],song_lib[song_list[-1]])
    return song_text

if __name__ == '__main__':
    common_str = 'Бабушка, бабушка, купим'
    song_lib = {'курочку':'Курочка по зёрнышку кудах-тах-тах','уточку':'Уточка та-ти-та-та','индюшонка':'Индюшонок фалды-балды',
            'кисоньку':'А кисуня мяу-мяу','собачонку':'Собачонка гав-гав','коровёнку':'Коровёнка муки-муки',
            'поросёнка':'Поросёнок хрюки-хрюки','телевизор':'Телевизор надо, надо, ведь у нас такое стадо!'}
    print(make_song(song_lib,common_str))