class Car:
    def drive(self):
        print("This car is moving?")
    def stop(self):
        print("This car has stopped")



class Astom_martin(Car):
    def drive(self):
        super().drive()  # Calling the drive method from the parent class
        print("This Aston Martin is moving fast!")


vehicle_1=Astom_martin()

vehicle_1.drive()