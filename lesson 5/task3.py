# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

# Вариант 1
print("Вариант 1")

total = 0
count = 0
employee = []
with open("test_file_task3.txt") as file:
    for line in file:
        salary = line.split(' ')
        if int(salary[1]) < 20000:
            employee.append(salary[0])
        total += int(salary[1])
        count += 1
result = total / count
print(f"Сотрудники с зарплатой меньше 20000: {employee}")
print(f"Средняя зарплата сотрудников: {result}")


# Вариант 2

print("Вариант 2")
with open('test_file_task3.txt') as file:
    workers = {}
    for line in file:
       key, value = line.split()
       workers[key] = value
       if float(value) < 20000:
            print(f'{key}: зарплата меньше 20000')