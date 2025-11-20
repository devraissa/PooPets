from models.pet import Pet

class Cat(Pet):
    def __init__(self, satiety, health, hygiene, happiness, rest, sleep_cycles, name="Bichinho"):
        super().__init__(satiety, health, hygiene, happiness, rest, sleep_cycles, name)

    def to_feed(self):
        self.set_satiety(value=25)
        return super().to_feed()

    def plays(self):
        self.set_happiness(value=30)
        self.set_rest(value=(-15))
        return super().plays()
    
    def sleeps(self):
        self.set_satiety(value=(-3))
        return super().sleeps()