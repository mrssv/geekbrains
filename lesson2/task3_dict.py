# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

seasons = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    print(f"Это {seasons.get(1)}")
elif month == 3 or month == 4 or month == 5:
    print(f"Это {seasons.get(2)}")
elif month == 6 or month == 7 or month == 8:
    print(f"Это {seasons.get(3)}")
elif month == 9 or month == 10 or month == 11:
    print(f"Это {seasons.get(4)}")
else:
    print("Ошибка! Укажите месяц цифрой от 1 до 12")