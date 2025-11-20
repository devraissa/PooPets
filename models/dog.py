from models.pet import Pet

class Dog(Pet):
    def __init__(self, satiety, health, hygiene, happiness, rest, sleep_cycles, name="Bichinho"):
        super().__init__(satiety, health, hygiene, happiness, rest, sleep_cycles, name)

    def to_feed(self):
        self.set_satiety(20)
        return super().to_feed()

    def plays(self):
        self.set_happiness(value=60)
        self.set_rest(value=(-30))
        return super().plays()
    
    def sleeps(self):
        self.set_satiety(value=(-8))
        return super().sleeps()

    def makes_sound(self):
        return "Au! Au!🐶🐾"
    
    