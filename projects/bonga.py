class Prey:
    alive = True

    def __init__(self, animal_type, species):
        self.type = animal_type
        self.species = species

    def killed(self):
        return f"This {self.type} is getting killed."


class Predator:
    alive = True

    def __init__(self, animal_type, species):
        self.type = animal_type
        self.species = species

    def eat(self):
        return f"This {self.type} is eating."


class Rabbit(Prey):
    def run(self):
        return f"This {self.type} is running."


class Lion(Predator):
    pass


lion_1 = Lion("lion", "panthera leo")
rabbit = Rabbit("Hare", "mono")

print(lion_1.eat())
print(rabbit.killed())
print(lion_1.alive)
print(rabbit.run())
