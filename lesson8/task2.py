# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):
    def __init__(self, text: str):
        self.text = text


try:
    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число:"))
    if b == 0:
        raise ZeroDivision("Ошибка. На ноль делить нельзя.")

    c = a / b
    print("a / b = ", c)

except ZeroDivision as err:
    if ZeroDivisionError:
        print(err)