class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def move(self):
        pass

    @staticmethod
    def create_animal(animal_type, name, species, **kwargs):
        if animal_type == "рыба":
            return Fish(name, species, **kwargs)
        elif animal_type == "птица":
            return Bird(name, species, **kwargs)
        elif animal_type == "млекопитающее":
            return Mammal(name, species, **kwargs)
        else:
            raise ValueError("Неверный тип животного")

class Fish(Animal):
    def __init__(self, name, species, water_type):
        super().__init__(name, species)
        self.water_type = water_type

    def make_sound(self):
        return f"{self.name} {self.species} издает булькающие звуки под водой."

    def move(self):
        return f"{self.name} {self.species} плывет в {self.water_type} воде."

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def make_sound(self):
        return f"{self.name} {self.species} чирикает и поет."

    def move(self):
        return f"{self.name} {self.species} летает с размахом крыльев {self.wingspan} дюймов."

class Mammal(Animal):
    def __init__(self, name, species, habitat):
        super().__init__(name, species)
        self.habitat = habitat

    def make_sound(self):
        return f"{self.name} {self.species} издает различные звуки."

    def move(self):
        return f"{self.name} {self.species} перемещается в своем месте обитания: {self.habitat}."

animal_type = "рыба"
name = "Немо"
species = "рыба-клоун"
water_type = "соленой"

new_animal = Animal.create_animal(animal_type, name, species, water_type=water_type)

print(new_animal.make_sound()) 
print(new_animal.move())
