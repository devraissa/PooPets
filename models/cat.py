from models.pet import Pet

class Cat(Pet):
    def __init__(self, name, satiety=50, health=100, hygiene=50, happiness=50, rest=100):
        super().__init__(name, satiety, health, hygiene, happiness, rest)

    def pet_plays(self):
        self.set_happiness(30)
        self.set_rest(-15)
        return super().pet_plays()
    
    def pet_sleeps(self):
        self.set_satiety(-3)
        return super().pet_sleeps()
    
    def pet_makes_sound(self):
        return "Miau! Miau!😸🐾"