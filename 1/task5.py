profit = int(input("Укажите выручку фирмы:"))
expenses = int(input("Укажите издержки фирмы:"))
if profit > expenses:
    print(f"Выручка фирмы больше издержек. Рентабельность выручки равна: {profit / expenses}")
    employees = int(input("Введите количество сотрудников фирмы:"))
    print(f"Прибыль фирмы в расчете на одного сторудника равна: {profit / employees}")
elif profit == expenses:
    print("Прибыль и издержки фирмы равны")
else:
    print("Фирма несет убытки")