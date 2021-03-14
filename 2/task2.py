#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().
test_list = []
el = 0
test_list.append(input("Введите значение 1:"))
test_list.append(input("Введите значение 2:"))
test_list.append(input("Введите значение 3:"))
test_list.append(input("Введите значение 4:"))
test_list.append(input("Введите значение 5:"))
for i in range(int(len(test_list) // 2)):
        test_list[el], test_list[el + 1] = test_list [el + 1], test_list[el]
        el += 2
print(test_list)