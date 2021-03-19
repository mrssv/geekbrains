# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

first_name = input("Введите имя пользователя: ")
last_name = input("Введите фамилию пользователя: ")
birth_year = input("Введите год рождения пользователя: ")
town = input("Введите город проживания пользователя: ")
email = input("Введите email пользователя: ")
tel = input("Введите телефон пользователя: ")


def person_data(first_name, last_name, birth_year, town, email, tel):
    return ' '.join([first_name, last_name, birth_year, town, email, tel])
print(person_data(first_name=first_name, last_name=last_name, birth_year=birth_year, town=town, email=email,tel=tel))



