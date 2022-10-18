playing_field = [[' '] * 3 for i in range(3)]
print(playing_field)
def field():
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {playing_field[i][0]} {playing_field[i][1]} {playing_field[i][2]}')

field()

def player_turn():
    while True:
        cell = input("Вы ходите в: ").split()
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
player_turn()