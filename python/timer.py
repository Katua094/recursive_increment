class Animal:

    Alive=True

    def eat(self):
        print("This animal is eating!!")
    
    def sleep(self):
        print("This animal is sleeping")




class Dog(Animal):
    def play(self):
        print("This dog is playing!")

class Cat(Animal):
    def meow(self):
        print("This Cat is meowing!!")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying look!!")



hawk=Hawk()

hawk.sleep()
hawk.fly()
cat=Cat
dog= Dog()

dog.eat()
dog.play()

print(cat.Alive)