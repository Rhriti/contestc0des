class Animal:
    def __init__(self):
        self.age=20

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self):
        self.age=99
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating instances of subclasses
dog = Dog()
cat = Cat()

print(dog.age)
print(cat.age)
dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows
