# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    args = [arg1, arg2, arg3]
    args.remove(min(arg1, arg2, arg3))
    return sum(args)


print(
    f'Сумма двух наибольших чисел: {my_func(int(input("Введите число 1: ")), int(input("Введите число 2: ")), int(input("Введите число 3: ")))}')
