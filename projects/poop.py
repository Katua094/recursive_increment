#objects as argurments

class Car:
    def __init__(self,name):
        self.name= name
    def __str__(self):
        return self.name


        
def color(vehicle,color):
    Car.color=color
    print(f"this {vehicle} is {color} in color.")

dodge=Car("dodge")

color(dodge,"red")
