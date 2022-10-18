playing_field = [[' '] * 3 for i in range(3)]
print(playing_field)
playing_field[0][1] = 'X'
def field():
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {playing_field[i][0]} {playing_field[i][1]} {playing_field[i][2]}')

field()