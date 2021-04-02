# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании
# экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.

class Road:
    _length: float
    _width: float

    bulk: float = 50
    thickness: float = 7

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_bulk(self, length, width):
        return length * width * Road.bulk * Road.thickness


street_length = float(input("Укажите длинну дороги в метрах: "))
street_width = float(input("Укажите ширину дороги в метрах: "))
street = Road(street_length, street_width)
print("Для постройки дороги указанных размеров потребуется: ", street.asphalt_bulk(street_length, street_width) / 1000, "тонн асфальта")