# Создайте программу для игры в ""Крестики-нолики"".

from unittest.mock import mock_open


lst = list(map(str, [i for i in range(1,10)]))
print(lst)
field = f'{lst[0]}-|{lst[1]}-|-{lst[2]}\n{lst[3]}-|{lst[4]}-|-{lst[5]}\n{lst[6]}-|{lst[7]}-|-{lst[8]}'
print(field)

def enter(marker):
    move = (input(f'Куда ставить (от 1 до 9) {marker}? '))
    while move != '1' and move != '2' and move !='3' and move != '4' and move != '5'\
        and move !='6' and move != '7' and move != '8' and move !='9': 
        move = (input(f'Выберите корректно номер хода(от 1 до 9) {marker}? '))
    if move == '1' and (lst[0] != 'X' and lst[0] != 'O'):
        lst[0] = marker
    elif move == '2'and (lst[1] != 'X' and lst[1] != 'O'):
        lst[1] = marker
    elif move == '3'and (lst[2] != 'X' and lst[2] != 'O'):
        lst[2] = marker
    elif move == '4'and (lst[3] != 'X' and lst[3] != 'O'):
        lst[3] = marker
    elif move == '5'and (lst[4] != 'X' and lst[4] != 'O'):
        lst[4] = marker
    elif move == '6'and (lst[5] != 'X' and lst[5] != 'O'):
        lst[5] = marker
    elif move == '7'and (lst[6] != 'X' and lst[6] != 'O'):
        lst[6] = marker
    elif move == '8'and (lst[7] != 'X' and lst[7] != 'O'):
        lst[7] = marker
    elif move == '9'and (lst[8] != 'X' and lst[8] != 'O'):
        lst[8] = marker
      

    field = f'{lst[0]}-|{lst[1]}-|-{lst[2]}\n{lst[3]}-|{lst[4]}-|-{lst[5]}\n{lst[6]}-|{lst[7]}-|-{lst[8]}'
    print(field)

count = 0
win = False
while not win:
    if not count%2:
        enter('X')
    else: 
        enter('O')
    count +=1
    if count > 4:
        if lst[0] == lst[1] == lst[2] or\
        lst[3] == lst[4] == lst[5] or\
        lst[6] == lst[7] == lst[8] or\
        lst[0] == lst[3] == lst[6] or\
        lst[1] == lst[4] == lst[7] or\
        lst[2] == lst[5] == lst[8] or\
        lst[0] == lst[4] == lst[8] or\
        lst[2] == lst[4] == lst[6]:
            win = True
            print('Вы победитель!')
        else:
            if count == 9:
                win = True
                print('Ничья!')

        


 










