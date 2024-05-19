adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
#""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
#треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
#""" Замініть .... на пробіл
#"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
#""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
#"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print (adwentures_of_tom_sawer)


# task 04
#""" Виведіть, скількі разів у тексті зустрічається літера "h"
#"""
print ("There are", adwentures_of_tom_sawer.count("h"), "letters 'H'")


# task 05
#""" Виведіть, скільки слів у тексті починається з Великої літери?
#"""
counter = 0
for i in adwentures_of_tom_sawer:
    if i.isupper(): 
        counter = counter + 1
print ("N. of capital letters is:", counter)

# task 06
#""" Виведіть позицію, на якій слово Tom зустрічається вдруге
#"""
c = adwentures_of_tom_sawer.find("Tom")
print ("The second word 'Tom' starts at the index:", adwentures_of_tom_sawer.find("Tom", c+1))

# task 07
#""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
#Збережіть результат у змінній adwentures_of_tom_sawer_sentences
#"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print (adwentures_of_tom_sawer_sentences)

# task 08
#""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
#Перетворіть рядок у нижній регістр.
#"""
print (adwentures_of_tom_sawer_sentences[4].lower())


# task 09
#""" Перевірте чи починається якесь речення з "By the time".
#"""
adwentures_of_tom_sawer_sentences = [item.strip() for item in adwentures_of_tom_sawer_sentences]
for item in adwentures_of_tom_sawer_sentences:  
    if item.startswith("By the time"): 
        found = True  
        break  


if found == True:
    print("At least one sentence starts with 'By the time'")

# task 10
#""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
#"""
last_sentence = adwentures_of_tom_sawer_sentences[-2]
print ("last sentence is","'", last_sentence, "'")
words = last_sentence.split()
word_count = len(words)
print("The last sentence has", word_count, "words.")