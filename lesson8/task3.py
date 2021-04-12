# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.

class StopExit(Exception):

    def __init__(self, new_list):
        self.new_list = new_list

    def __str__(self):
        return f'Завершение, выш список: {self.new_list}'


class UserList:

    @staticmethod
    def create_user_list():
        new_list = []
        while True:
            my_list = input('Введите число или "stop" для выхода: ')
            if my_list.isdigit():
                new_list.append(my_list)
                print(new_list)
            elif my_list == 'stop':
                raise StopExit(new_list)
            elif not my_list.isdigit():
                print(f'Вы ввели строку, введите число')


try:
    print(UserList.create_user_list())
except StopExit as error:
    print(error)