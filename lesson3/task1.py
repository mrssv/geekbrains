# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа
# запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(*numbers):
    try:
        number1 = int(input("Введите число 1:"))
        number2 = int(input("Введите число 2:"))
        result = number1 / number2
    except ZeroDivisionError:
        return "На ноль делить нельзя"

    return result


print(f"Ответ: {division()}")
