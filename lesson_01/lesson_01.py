# Приклади виконання найпростіших команд із консолі інтерпретатора

# Створення найпростішої програми та збереження її у файл
print("Hello world!")
# Запуск збереженого файлу на виконання

# Що таке IDE і навіщо воно треба

# Змінні (Variables), створення та використання змінних
# Заборонені символи у змінних

user_name = "Alex"
print(user_name)

user_age = 38

name_for_variable = "abcde"

# Відступи (Indentation)

user_age = user_age + 1
print(user_age)


my_previous_age = user_age - 1
print("my_previous_age:", my_previous_age)

# Вивід даних через print()
user_age = 17
if user_age >= 18:
    print("Congratulations, you are no longer a teenager!")
    print("ok")
print("not ok")

for i in user_name:
    print(i)

print("game over")


# Найпростіші математичні операції:
# додавання, віднімання, множення
a = 7
b = 3
summ = a + b  # Додавання
diff = a - b  # Віднімання
mult = a * b  # Множення
divd = a / b  # Ділення

# print(object(s)*, sep=*separator*, end=*end*, file=*file*, flush=*flush*)
print(summ, diff, mult, divd, sep=",\n", end="\n")
print("next line")
