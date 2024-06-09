# ####["1,2,3,4",
#     "1,2,3,4,50"
#     "qwerty1,2,3"]
    
#     Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
    
#     Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
    
#     Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
    
#     Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

test_list = ["1,3,5,7,9", "2,4,6,8,10", "1,2,3,4,5,6,7,8,9,10", "abcdef"]
#test_list = ["1,3,5,7,9", "2,4,6,8,10", "1,2,3,4,5,6,7,8,9,10"]
#test_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def list_calk (str_list):
    """Calculates sum of the numbers in string, removes comas"""
    counter = []
    try:
        for i in str_list:
            num_st = i.split(",")
            num = [int(n) for n in num_st]
            num_sum = sum(num)
            counter.append(num_sum)
        
    except ValueError:
        counter.append('Не можу це зробити')
    finally:
        return (counter)
task = list_calk(test_list)
print (task)

