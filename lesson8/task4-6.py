# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class EquipmentWarehouse:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства:': self.name, 'Цена за ед.:': self.price, 'Количество:': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за ед.: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства:': unit, 'Цена за ед:': unit_p, 'Количество:': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список: \n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Нажмите Q для выхода или Enter для продолжения')
        q = input(f' ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад: \n {self.my_store_full}')
            return f'Выход'
        else:
            return EquipmentWarehouse.reception(self)


class Printer(EquipmentWarehouse):
    def to_print(self):
        return f'Чтобы распечатать {self.numb} раз'


class Scanner(EquipmentWarehouse):
    def to_scan(self):
        return f'Чтобы отсканировать {self.numb} раз'


class Copier(EquipmentWarehouse):
    def to_copier(self):
        return f'Чтобы скопировать  {self.numb} раз'


unit_1 = Printer('hp', 5000, 5, 10)
unit_2 = Scanner('Canon', 5000, 5, 10)
unit_3 = Copier('Xerox', 5000, 5, 10)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
