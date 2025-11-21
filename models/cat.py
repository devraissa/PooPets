from models.pet import Pet

class Cat(Pet):
    """ Representa o Pet Gato. Herda todas as funcionalidades e atributos da classe Pet (PetBase). """

    def __init__(self, satiety, health, hygiene, happiness, rest, sleep_cycles, name="Bichinho"):
        super().__init__(satiety, health, hygiene, happiness, rest, sleep_cycles, name)

    def to_feed(self):
        # O Gato tem um ganho de Saciedade maior (25) do que o padrão, refletindo sua maior eficiência na alimentação.
        self.set_satiety(value=25)
        return super().to_feed()

    def plays(self):
        # O Gato é menos ativo, ganhando menos felicidade e gastando pouca energia.
        self.set_happiness(value=30)
        self.set_rest(value=(-15))
        return super().plays()
    
    def sleeps(self):
        # O Gato tem uma perda de Saciedade muito baixa (-3) ao acordar, refletindo seu metabolismo lento e sua capacidade de hibernar.
        self.set_satiety(value=(-3))
        return super().sleeps()