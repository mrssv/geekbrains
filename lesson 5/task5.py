# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

with open('test_file_task5.txt', 'w') as file:
            numbers = input('Введите числа через пробел:')
            file.writelines(numbers)
            number = numbers.split()
            print(sum(map(int, number)))