from models.pet import Pet

class Dog(Pet):
    """ Representa o Pet Cachorro. Herda todas as funcionalidades e atributos da classe Pet (PetBase). """

    def __init__(self, satiety, health, hygiene, happiness, rest, sleep_cycles, name="Bichinho"):
        super().__init__(satiety, health, hygiene, happiness, rest, sleep_cycles, name)

    def to_feed(self):
        # O Cachorro usa o ganho de Saciedade padrão (20).
        self.set_satiety(value=20)
        return super().to_feed()

    def plays(self):
        # O Cachorro é o mais brincalhão, ganhando muita felicidade e gastando muita energia (Descanso).
        self.set_happiness(value=60)
        self.set_rest(value=(-30))
        return super().plays()
    
    def sleeps(self):
        # Define o alto custo de Saciedade (fome) que o Cachorro terá ao acordar, devido ao seu metabolismo ativo.
        self.set_satiety(value=(-8))
        return super().sleeps()
    