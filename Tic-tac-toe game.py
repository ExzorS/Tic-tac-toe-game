def ruls():
    print('Правила игры Крестики-Нолики')
    print('-------------------------------------------------------')
    print('Два игрока по очереди ставят Х или О')
    print('Символы в поле ставятся с помощью координат')
    print('Первая координата отвечает за строки')
    print('Вторая координата отвечает за столбцы')
    print('Первый, выстроивший в ряд 3 своих символа по вертикали,'
          '\nгоризонтали или диагонали, выигрывает')
    print('Первый игрок ставит Х')
    print('-------------------------------------------------------')

ruls()

playing_field = [[' '] * 3 for i in range(3)]
def field():
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {playing_field[i][0]} {playing_field[i][1]} {playing_field[i][2]}')

def player_turn():
    while True:
        cell = input('Вы ходите в: ').split()
        if len(cell) != 2:
            print('Введите 2 координаты через пробел!')
            continue

        x, y = cell

        if x.isdigit() or y.isdigit():
            x, y = map(int, cell)
        else:
            print('Введите числа!')
            continue

        if 0 <= x <= 2 and 0 <= y <= 2:
            if playing_field[x][y] == ' ':
                return x, y
            else:
                print('Клетка уже занятя.')
        else:
            print('Почти попали в поле, попробуйте ещё раз =)')

move_number = 0

while True:
    move_number += 1

    field()

    if move_number % 2 == 1:
        print('   Ходит Х')
    else:
        print('   Ходит О')

    x, y = player_turn()

    if move_number % 2 == 1:
        playing_field[x][y] = 'X'
    else:
        playing_field[x][y] = 'O'

    if win():
        break

    if move_number == 9:
        print('Ничья')
        break

def win():
    winning_combination = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for combination in winning_combination:
        a = combination[0]
        b = combination[1]
        c = combination[2]

        if playing_field[a[0]][a[1]] == playing_field[b[0]][b[1]] == playing_field[c[0]][c[1]] != ' ':
            print(f'Победил {playing_field[a[0]][a[1]]}!')
            return True
        return False


