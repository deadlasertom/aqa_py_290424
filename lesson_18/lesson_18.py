

class MyIterator():
    def __init__(self, end, step: int = 2) -> None:
        self.end = end
        self.step = step
        self.current = 0

    
    def __iter__(self):
        return self


    def __next__(self):
        if self.current <= self.end:
            output = self.current
            self.current += self.step
            return output
        else:
            raise StopIteration

def my_for(iterable, callback_func):
    iterator = iter(iterable)
    while True:
        try:
            value = next(iterator)
            callback_func(value)
        except StopIteration:
            break

def my_for_2(iterable):
    iterator = iter(iterable)
    while True:
        try:
            value = next(iterator)
            yield value
        except StopIteration:
            break

def super_print(s:str):
    print(s*8)

print("=======")
my_for('bye', super_print)
print("=======")
bbye = my_for_2('bye')
for i in bbye:
    super_print(i)
print("=======")

if __name__ == "__main__":
    my_iterator = MyIterator(10, 3)

    # for i in my_iterator:
    #     print(i)
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    # print(next(my_iterator))  ##  raise StopIteration 
    print("*")
  
