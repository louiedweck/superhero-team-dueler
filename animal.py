class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{} is eating'.format(self.name))

    def drink(self):
        print('{} is drinking'.format(self.name))


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")


my_dog = Dog("Sophie")
my_dog.bark()
