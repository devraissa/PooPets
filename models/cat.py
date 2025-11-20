from models.pet import Pet

class Cat(Pet):
    def __init__(self, satiety, health, hygiene, happiness, rest, sleep_cycles, name="Bichinho"):
        super().__init__(satiety, health, hygiene, happiness, rest, sleep_cycles, name)

    def plays(self):
        self.set_happiness(value=30)
        self.set_rest(value=(-15))
        return super().plays()
    
    def sleeps(self):
        self.set_satiety(value=(-3))
        return super().sleeps()
    
    def makes_sound(self):
        return "Miau! Miau!😸🐾"