import time
# Отримуємо поточний час у вигляді кортежу
current_time = time.localtime()
print(current_time)
print("Year", current_time.tm_year)
print("Month", current_time.tm_mon)
# DST - Daylight Saving Time — це англомовне позначення переходу на літній час
some_time = time.asctime((1980, 1, 2, 3, 4, 5, 6, 7, 8))
print(some_time)
my_real_time = time.asctime()
my_real_time_2 = time.asctime(time.localtime())
print("my time", my_real_time)
print(my_real_time == my_real_time_2)
# час епохи
print(time.ctime(0))
nix_time_now = time.ctime(1686547846)
print(nix_time_now)
time_now =time.ctime(1722270782)
print(time_now)
print(time.time())
time.sleep(0.5) # НАЙЖАХЛИВІШИЙ СПОСІБ !!
print(time.time())

good_time_output = time.strftime("Now year %Y %m month and day is %d time is: %H:%M",
                     time.localtime())
print(good_time_output)

print(time.strptime("Sep 20, 2022", '%b %d, %Y'))
print(time.strptime("19:45:55", '%H:%M:%S'))

# Рядок з часом
time_string = '2023-12-31 23:59:59'
# Формат рядка
format_string = '%Y-%m-%d %H:%M:%S'
# Перетворення рядка у структуру часу
time_obj = time.strptime(time_string, format_string)
print(time_obj)
