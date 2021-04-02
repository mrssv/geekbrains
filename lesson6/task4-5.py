# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# 5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print("Машина поехала.")

    def car_stop(self):
        print("Машина остановилась.")

    def car_right(self):
        print("Машина повернула направо.")

    def car_left(self):
        print("Машина повернула налево.")

    def car_show_speed(self):
        print(f"Скорость машины {self.speed} км/ч")


class TownCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def car_show_speed(self):
        print("Это городская машина.")
        print(f"Скорость машины {self.speed} км/ч")
        if self.speed > 60:
            print("Машина превысила допустимую скорость.")


class WorkCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def car_show_speed(self):
        print("Это рабочая машина.")
        print(f"Скорость машины {self.speed} км/ч")
        if self.speed > 40:
            print("Машина превысила допустимую скорость.")


class SportCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(80, "черный", "Mazda", False)
car1.car_show_speed()
print("Цвет машины", car1.color)
print("Марка машины", car1.name)
print()
car2 = WorkCar(50, "синий", "Volvo", False)
car2.car_show_speed()
print("Цвет машины", car2.color)
print("Марка машины", car2.name)
print()
car3 = SportCar(180, "красный", "Ferrari", False)
print("Это спортивная машина.")
car3.car_show_speed()
print("Цвет машины", car3.color)
print("Марка машины", car3.name)
print()
car4 = PoliceCar(60, "белый", "Chevrolet", True)
print("Это полицеская машина.")
car4.car_show_speed()
print("Цвет машины", car4.color)
print("Марка машины", car4.name)