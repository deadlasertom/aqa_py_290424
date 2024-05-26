small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
small_list_u = []
for i in small_list:
    if small_list.count(i) == 1:
     small_list_u.append(i)

print ("Unique items in small list:", small_list_u)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
#small_list_count = small_list.count
small_list_count  = 0
for i in small_list:
    small_list_count  = small_list_count +1

small_list_sum = sum(small_list)
print (f"Small list avarage is {small_list_sum/small_list_count}")


# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
big_list_set = set(big_list)

big_list_count  = 0
for i in big_list:
    big_list_count  = big_list_count +1

big_list_set_count  = 0
for i in big_list_set:
    big_list_set_count  = big_list_set_count +1

if big_list_set_count == big_list_count:
    print ("There are no dublicates in big list");
else:
    print ("There are dublicates in big list")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
big_key = 0
for i in add_dict.values():
    if i >= big_key:
        big_key = i
print (f"{big_key} is maximal value key in 'add_dict'")


# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
# Не уверен, что правильно понял задание, поэтому поменял значения и ключи местами.


new_dict = {}
for key, value in add_dict.items():
    new_dict [value] = key
print ("Task 5: new_dict:", new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
sum_dict = base_dict.copy()
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value
print("Task 6 - sum_dict:", sum_dict)

# task 7.
#Если я правильно понял, то тут нужно сделать сет с символами из переменной line
line = "Створіть множину всіх символів, які входять у заданий рядок"
line_symbols = set(line)
print ("Task 7 - line_symbols:", line_symbols)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

set_3 = set()
for i in set_1:
    if i in set_2:
        continue
    else:
        set_3.add(i)
for i in set_2:
    if i in set_1:
        continue
    else:
        set_3.add(i)
counter = 0
for i in set_3:
    counter = counter + i
print("Task 8 - Sum of all unique symbols:", counter)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

new_set = set()
for i in list_1:
    if i in list_2:
        continue
    else:
        new_set.add(i)
for i in list_2:
    if i in list_1:
        continue
    else:
        new_set.add(i)
print("Task 9 - Set with all unique symbols from list_1 and list_2:", new_set)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

persons_list_dict = {'10-19': [], '20-29': [], '30-39': [], '40-49': [], '50-59': []} 
for n, a in person_list:
    if a >= 10 and a <= 19:
        age_range = '10-19'
    elif a >= 20 and a <= 29:
        age_range = '20-29'
    elif a >= 30 and a <= 39:
        age_range = '30-39'
    elif a >= 40 and a <= 49:
        age_range = '40-49'
    elif a >= 50 and a <= 59:
        age_range = '50-59'
    #etc
    
    persons_list_dict[age_range].append(n)
print(persons_list_dict)
