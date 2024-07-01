

# LEGB - Local, Enclosing, Global, Built-in

# Local
def run(a):
    a = 2
    return a + 1


PDV = 20
class MyBuh():
    b = 5  # Enclosing

    def count(self):
        print(self.b)
        print("ПДВ:", PDV)  # Global

# Built-in
# y = 10
def outer_function():
    y = 20
    def inner_function():
        # y = 30
        print(y)
    inner_function()



if __name__ == "__main__":
    print(run(1))
    coun_buh = MyBuh()
    coun_buh.count()
    print(PDV)
    coun_buh.new_attr = 5
    print(coun_buh.new_attr)
    outer_function()
    print(len("Hello Word"))
