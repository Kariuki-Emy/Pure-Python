class Animal:
    def __init__(self, name):
        self.myname = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return "meow"


class Dog(Animal):
    def talk(self):
        return "woof"


class sheep(Animal):
    def talk(self):
        return "bleets"


paka = Cat("Whiskers")
doggy = Dog("Bark")
kondoo = sheep("leo")
print(paka.myname + " :" + paka.talk())
print(doggy.myname + " :" + doggy.talk())
print(kondoo.myname + " :" + kondoo.talk())
