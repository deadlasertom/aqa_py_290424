a = 1
b = 1

print(a > b)  # False
print(a >= b)  # False
print(a == b)  # False
print(a <= b)  # True
print(a < b)   # True

if a > b:
    print("A lage then B")
    a = a + b
elif a == b:
    print("A equal B")
elif a < b:
    print("B lage then A")
else:
    print("A not lage then B")
print(a)

telephone = "+380990001122"  # "" #
email =  "sobake@gmail.com"  # "" #

if telephone != "" and email != "":
    print("All fine, no action need here")
elif telephone == "" and email == "":
    telephone = input("Put you phone number, please:")
    email = input("Enter your email, please:")
elif email == "":
    email = input("Enter your email, please:")
else:
    telephone = input("Put you phone number, please:")
print(telephone, email)

selenium=1
playwrite=0

if selenium > 1 or playwrite > 1:
    print("Good candidate!!")
else:
    print("Looking next one")

age = 25
is_student = True
has_experience = False

if (age >= 18 and is_student) or (has_experience and age < 30):
    print("You are either an adult student or have experience and are under 30.")
else:
    print("You don't meet any of the specified conditions.")

count = 0
while count < 5:
    print(count) #"*" *
    count += 1

print("*"*88)

number_list = [3, 6, 4, 3, 5, 3, 3, 2, 4, 1, 4, 5]
for i in number_list:
    if i % 2 == 0:
        print(i)
    else:
        print(">>>", i)
end = len(number_list)

print("while*")
while end > 0:
    end = end - 1
    i = number_list[end]
    if i % 2 == 0:
        print(i)
    else:
        print(">>>", i)

for i in range(0, 20):
    if i in [16, 14, 10, 8]:
        continue
    elif i == 13:
        break
    print("R", i)

for num in range(0,17):
    for base in 'dfxob':
        print('{0:{width}{base}}'.format(num, base=base, width=6), end=' ') # {num:6x}
    print()


target_value = 7
for i in range(10):
    if i == target_value:
        print("Знайдено шукане значення:", i)
        break
    print(i)

for i in range(10):
    if not (i % 2):
        continue
    print("Непарне число:", i)

my_list = [7, 2, 4, 4, 5, 6, 3, 8, 9]
new_list = [i for i in my_list if i % 3 == 0]
# new_list = []
# for i in my_list:
#     if i % 3 == 0:
#         new_list.append(i)

print(new_list)