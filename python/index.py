class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

# Function that expects an object with a 'speak' method
def animal_sound(animal):
    return animal.speak()

# Instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()

# All these objects can be passed to the function
print(animal_sound(dog))  # Outputs: Woof!
print(animal_sound(cat))  # Outputs: Meow!
print(animal_sound(duck)) # Outputs: Quack!
