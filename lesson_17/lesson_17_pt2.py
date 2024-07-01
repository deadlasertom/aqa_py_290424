
def igigo():
    return "megogo"

class Horse:
    def run(self):
        return "Я біжу!"
    
    def say(self):
        return "Кінь, просто кінь. Дуже приємно, кінь!"
    
    def igigo(self):
        return "Igogo"


class Eagle:
    def fly(self):
        return "I can fly!!"
    
    def say(self):
        return "Юний орел, юний орел що летить від джерел до..."


class Pegasus(Eagle, Horse):
    def say(self):
        return "UNICORN!!!!!!!"



if __name__ == "__main__":
    pinky_pie = Pegasus()
    print(pinky_pie.fly())
    print(pinky_pie.run())
    print(pinky_pie.say())
    print(pinky_pie.igigo())
    print(igigo())
