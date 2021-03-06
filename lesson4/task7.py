# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые
# n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial


def factorial_func(num):
    for el in range(1, num + 1):
        yield factorial(el)


try:
    fact_number = int(input("Укажите значение для расчета факториала: "))
    for el in factorial_func(fact_number):
        print(el, end=" ")
except ValueError:
    print("Укажите числовое значение")


