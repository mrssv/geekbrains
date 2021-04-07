# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных
# данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.

from abc import ABC, abstractmethod


class AbsGarments(ABC):
    @abstractmethod
    def coat_cloth(self):
        pass

    @abstractmethod
    def suit_cloth(self):
        pass

    @abstractmethod
    def total_cloth(self):
        pass


class Garments(AbsGarments):
    def __init__(self, size: int, height: int):
        self.size = size
        self.height = height

    @property
    def coat_cloth(self):
        return round(self.size / 6.5 + 0.5, 1)

    @property
    def suit_cloth(self):
        return round(self.size * 2 + 0.3, 1)

    @property
    def total_cloth(self):
        return f'{round(self.size / 6.5 + .5, 1) + round(self.size * 2 + .3, 1)}'


my_clothes = Garments(48, 170)
print(f'Для пальто требуется {my_clothes.coat_cloth} м2 ткани')
print(f'Для костюма требуется {my_clothes.suit_cloth} м2 ткани' )

print(f'Итого требуется {my_clothes.total_cloth} м2 ткани')
