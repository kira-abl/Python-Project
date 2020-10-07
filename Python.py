def hi():
    print("Hello Mr. Jones! How are you today?")

hi()
hi()
hi()


def hiYou(name):
    print("Hello " + name + "! How are you today?")

hiYou("John")
hiYou("James")
hiYou("Maggie")

def hiMe(name="sir"):
    print("Hello " + name + "! How are you today?")

hiMe()
hiMe("James")

class Car:

    def __init__(self, mod, max_speed):
        self.model = mod
        self.max_speed = max_speed
        self.speed = 0

bmw_x6 = Car(mod="BMW X6", max_speed=230)

print(bmw_x6.model)
print(bmw_x6.max_speed)
print(bmw_x6.speed)
