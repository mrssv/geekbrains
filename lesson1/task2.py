# user = input ("Введите Ваше имя:")
# print("Привет, %s!" % user)
time_in_seconds = int(input("Укажите время в секундах:"))
hours = (time_in_seconds // 3600)
minutes = ((time_in_seconds % 3600) // 60)
seconds = ((time_in_seconds % 60) % 60)
time = (f"{hours}:{minutes}:{seconds}")
#как вариант time = ("{}:{}:{}".format(hours, minutes, seconds))
print(time)
