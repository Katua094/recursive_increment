class Rectangle:
    def __init__(self,width,length):
        self.height=width
        self.length=length
    

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.length
    
class Cube(Rectangle):
    def __init__(self,height,length,width):
        self.height=height
        super().__init__(width,length)
    def volume(self):
        return self.height*self.length*self.length


square=Square(3,3)

cube=Cube(3,3,3)

print(cube.volume())
print(square.area())

