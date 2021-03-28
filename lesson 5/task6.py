# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}
with open('test_file_task6.txt') as file:
    for line in file:
        subject = line.split()
        for i in range(len(subject)):
            if subject[i] == '-':
                subject[i] = "0"

        subject_title = subject[0].replace(':', '')
        lectures = subject[1].replace('(л)', '')
        practice = subject[2].replace('(пр)', '')
        lab = subject[3].replace('(лаб)', '')
        total_hours = int(lectures) + int(practice) + int(lab)
        my_dict.update({subject_title: total_hours})
print(my_dict)
