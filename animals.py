class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

def make_noise(animal):
    return animal.speak()