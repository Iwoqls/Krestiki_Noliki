map_ = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# цифры  1    2    3    4    5    6    7    8    9

# Выигрышные комбинации

combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
         [0, 3, 6], [1, 4, 7], [2, 5, 8],
         [0, 4, 8], [2, 4, 6]]


# Определение победителя

def wineer():
    for line in combo:
        if map_[line[0]] == map_[line[1]] == map_[line[2]] == 'X':
            print('\nПобедил X')
            exit()
        if map_[line[0]] == map_[line[1]] == map_[line[2]] == 'O':
            print('\nПобедил O')
            exit()


# Приветствие и показ игрового поля

def greeting():
    print('')
    print('Добро пожаловать в игру!')
    print('   КРЕСТИКИ - НОЛИКИ')
    print('')
    print('Игровое поле выглядит так:')
    for i in range(3):
        print('|', map_[0 + i * 3], '|', map_[1 + i * 3], '|', map_[2 + i * 3], '|')


# Вывод игрового поля

def print_board():
    for i in range(3):
        print('|', map_[0 + i * 3], '|', map_[1 + i * 3], '|', map_[2 + i * 3], '|')


# Проверка на символы в поле

def check_number(number):
    if map_[number] == '-':
        return True
    else:
        return False


# Проверка на ничью

def check_map():
    if '-' in map_:
        return True
    else:
        exit('\n\n\n\n\n\nНичья!')


# Ход игроков

def player_step(tag):
    while True:
        step = int(input('\nХОДИТ ' + tag + '.\nВведите куда поставить от 1 до 9: ')) - 1
        if step in range(0, 9):
            if check_number(step):
                map_[step] = tag
                break
            else:
                print('Ячейка занята, выберете другую!')
        else:
            print('\nВведите число от 1 до 9')


# Основная функция игры

def main():
    greeting()
    while True:
        player_step('X')
        print_board()
        wineer()
        check_map()
        player_step('O')
        print_board()
        wineer()
        check_map()


main()
