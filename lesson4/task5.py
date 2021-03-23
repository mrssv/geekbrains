# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#  Подсказка: использовать функцию reduce().

from functools import reduce

number_list = [el for el in range(99, 1001) if el % 2 == 0]
print(f'Список четных значений от 100 до 1000: {number_list}')


def number_multiply(el0, el1):
    return el0 * el1


print(f'Результат вычисления произведения всех элементов списка: {reduce(number_multiply, number_list)}')
