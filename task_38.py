# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def show():
    file = open('data.txt', 'r', encoding='utf-8')
    book = file.read()
    return book

def add():
    file = open('data.txt', 'a', encoding='utf-8')
    file.write(input('Введите строку: '+ '\n') )
    

def find():
    file = open('data.txt', 'r', encoding='utf-8')
    book = file.read().split('\n')
    temp = input('Поиск:    ')
    for i in book:
        if temp in i:
            print(i)


def delete(name):
    file = open("data.txt", "w", encoding="utf8" )
    persons = file.read().split('\n')
    for person in persons:
        if name != person:
            file.write(person)

def change(new_name, old_name):
    file = open("data.txt", "w", encoding="utf8" )
    persons = file.read().split('\n')
    for person in persons:
        if  old_name != person:
            file.write(person)
        else:
            file.write(new_name + "\n")

while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show())
    elif mode == '0':
        find()
    elif mode == '2':
        add()
    elif mode == '3':
        name = input('удалить:      ')
        delete(name)
    elif mode == '4':
        old_name = input(' переименовать:       ')
        new_name = input('Новое имя:        ')
        change(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('error')