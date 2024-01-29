#Abstract Methods
from abc import ABC ,abstractmethod

class parent(ABC):
    @abstractmethod
    def eat(self):
        print("This madafaka is eating.")
    @abstractmethod    
    def sleep(self):
        print("This nigga is sleeping.")


class Child(parent):
    pass
try:

    object=Child()

    object.eat()

except TypeError:
    print("Write individual methods of the child")