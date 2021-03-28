# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open("test_file_task2.txt") as file:
    lines = 0
    words = 0
    for line in file:
        lines += line.count("\n")
        words = len(line.split())
        print(f"В данной строке {words} слов")
    print(f"Итого в файле {lines} строк(и)")

