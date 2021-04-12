# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def extract_data(cls, date):
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[6:10])
        print("Day:", day, "Month:", month, "Year:", year)
        return day, month, year

    @staticmethod
    def validate_data(date: str):
        if int(date[:2]) > 31:
            print("Неверно указано число месяца")
        if int(date[3:5]) > 12:
            print("Неверно указан месяц")
        if int(date[6:10]) < 1900 or int(date[6:10]) > 2021:
            print("Неверно указан год")


a = input("Введите дату в формате ДД-ММ-ГГГГ: ")
Data.extract_data(a)
Data.validate_data(a)