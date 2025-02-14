class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract metod.")


class Dog(Animal):
    def speak(self):
        return f"{self.name} говори ГАВ!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит МЯУ!"


dog = Dog("Бобик")
cat = Cat("Мурзик")

print(dog.speak())
print(cat.speak())
