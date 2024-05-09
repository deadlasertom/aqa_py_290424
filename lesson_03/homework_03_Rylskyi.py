# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?" ' \
    '"That depends a good deal on where you want to get to," said the Cat. ' \
    '"I don\'t much care where ——" said Alice. ' \
    '"Then it doesn\'t matter which way you go," said the Cat. ' \
    '"—— so long as I get somewhere," Alice added as an explanation. ' \
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)

#"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
#"""
# task 04
#"""
#Площа Чорного моря становить 436 402 км2, а площа Азовського
#моря становить 37 800 км2. Яку площу займають Чорне та Азов-
#ське моря разом?
#"""
blacksea = 436402
azovsea = 37800
print ("Total are of Azov and Black Seas is", blacksea + azovsea, "square kilometers.")

# task 05
#"""
#Мережа супермаркетів має 3 склади, де всього розміщено
#375 291 товар. На першому та другому складах перебуває
#250 449 товарів. На другому та третьому – 222 950 товарів.
#Знайдіть кількість товарів, що розміщені на кожному складі.
#"""

first_and_second = 250449
third_and_second = 222950
total = 375291
first_s = total-third_and_second
third_s = total-first_and_second
second_s = first_and_second-first_s
print ("There are:", first_s, "units in the first warehouse,", second_s, "units in the second warehouse and", third_s, "units in the third warehouse.")


# task 06
#"""
#Михайло разом з батьками вирішили купити комп’ютер, ско-
#риставшись послугою «Оплата частинами». Відомо, що сплачу-
#вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
#вартість комп’ютера.
#"""

print ("Total cost of the PC is:", 1179*(12*1.5), end=" UAH.")


# task 07
#"""
#Знайди остачу від діленя чисел:
#a) 8019 : 8     d) 7248 : 6
#b) 9907 : 9     e) 7128 : 5
#c) 2789 : 5     f) 19224 : 9
#"""

a= 8019 % 8
b= 9907 % 9 
c= 2789 % 5 
d= 7248 % 6
e= 7128 % 5
f= 19224 % 9
print ("The remainders of dividing are following: ", "a)", a, " b)", b, " c)", c, " d)", d, " e)", e, " f)", f, sep="" )

# task 08
#"""
#Іринка, готуючись до свого дня народження, склала список того,
#що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
#для даного її замовлення.
#Назва товару    Кількість   Ціна
#Піца велика     4           274 грн
#Піца середня    2           218 грн
#Сік             4           35 грн
#Торт            1           350 грн
#Вода            3           21 грн
#"""

c_pizza_b = 274 * 4
c_pizza_m = 218 * 2
c_juice = 35 * 4
cake = 350
c_water = 21 * 3
print ("For her birthday, Irene needs", c_pizza_b + c_pizza_m + c_juice + cake + c_water, "UAH in total.")

# task 09
#"""
#Ігор займається фотографією. Він вирішив зібрати всі свої 232
#фотографії та вклеїти в альбом. На одній сторінці може бути
#розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
#Ігорю, щоб вклеїти всі фото?
#"""

pages = 232 / 8
pages_2 = (-1 * pages // 2 * -1) #самый простой способ округления в большую сторону, который я нашел.
print ("Igor will need album with at least", pages_2, "pages, providing that pages can be used from both sides," \
        " or album with", pages, "pages if photos can be added only to one side of the page.")

# task 10
#"""
#Родина зібралася в автомобільну подорож із Харкова в Буда-
#пешт. Відстань між цими містами становить 1600 км. Відомо,
#що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
#становить 48 літрів.
#1) Скільки літрів бензину знадобиться для такої подорожі?
#2) Скільки щонайменше разів родині необхідно заїхати на зап-
#равку під час цієї подорожі, кожного разу заправляючи пов-
#ний бак?
#"""

t_fuel = 1600 / 100 * 9
print (t_fuel)
stops = t_fuel / 48
print ("The family will need at least", t_fuel, "liters of fuel, and refuel car", stops, "times.")
