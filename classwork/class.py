# class Avenger():
#     def fight(self, name):
#         print(f"Avenger {name} is fighting")

#     def introduce(self, name):
#         print(f"my name is {name} ")

# ironman=Avenger()
# hulk=Avenger()

# ironman.fight("Ironman")

# hulk.fight("Hulk")
# ironman.introduce("a")


class car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

c=car("a","b")
print(c.brand, c.model)


class animal:
    def sound(self):
        print("hi")

class dog(animal):
    def sound(self):
        print("hello")

d=dog()
d.sound()