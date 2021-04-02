# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса
# Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
# примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = None
    surname = None
    position = None
    profit = None
    reward = None

    def __init__(self, name, surname, position, profit, reward):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.reward = reward


class Position(Worker):
    def __init__(self, name, surname, position, profit, reward):
        super().__init__(name, surname, position, profit, reward)

    def get_full_name(self):
        return self.name + self.surname

    def get_full_profit(self):
        self.__income = {'profit': self.profit, 'bonus': self.reward}
        return self.__income


manager = Position('Andrew ', 'Manson', 'engineer', 1000, 350)
print(manager.get_full_name(), manager.get_full_profit())
