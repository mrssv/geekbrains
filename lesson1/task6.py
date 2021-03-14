a = int(input("Укажите, сколько километров спортсмен пробежал в первый день: "))
b = int(input("Укажите целевую дистанцию в километрах: "))
day = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        day += 1
        result_km = result_km + a
print(f"На {day}й день спортсмен достиг результата — не менее {b} км.")