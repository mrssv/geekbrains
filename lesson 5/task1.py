# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

list = []
while True:
    line = input("Введите текст:")
    if line == '':
        print(list)
        exit()
    else:
        newline = line
        list.append(newline)

    with open("test_1.txt", "w") as file:
        file.writelines("%s\n" % line for line in list)
