from models.pet import Pet

class Dog(Pet):
    def __init__(self, name, satiety=50, health=100, hygiene=50, happiness=50, rest=100):
        super().__init__(name, satiety, health, hygiene, happiness, rest)

    def pet_plays(self):
        self.set_happiness(60)
        self.set_rest(-30)
        return super().pet_plays()
    
    def pet_sleeps(self):
        self.set_satiety(-8)
        return super().pet_sleeps()

    def pet_makes_sound(self):
        return "Au! Au!🐶🐾"
    
    