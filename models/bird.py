from models.pet import Pet

class Bird(Pet):
    """ Representa o Pet Passarinho. Herda todas as funcionalidades e atributos da classe Pet (PetBase). Sobrescreve métodos específicos para refletir seu comportamento de metabolismo acelerado (alto gasto de energia e rápida satisfação). """

    def __init__(self, satiety, health, hygiene, happiness, rest, sleep_cycles, name="Bichinho"):
        super().__init__(satiety, health, hygiene, happiness, rest, sleep_cycles, name)
    
    def to_feed(self):
        # Sobrescrita do método to_feed(). O Passarinho tem uma taxa de satisfação diferente (come menos).
        self.set_satiety(value=15)
        return super().to_feed()

    def plays(self):
        # Sobrescrita do método plays(). O Passarinho é o mais brincalhão e gasta muita energia, ganhando muita felicidade.
        self.set_happiness(value=70)
        self.set_rest(value=(-40))
        return super().plays()
    
    def sleeps(self):
        # Sobrescrita do método sleeps(). Define o alto custo de Saciedade (fome) que o Passarinho terá ao acordar, devido ao seu metabolismo acelerado.
        self.set_satiety(value=(-12))
        return super().sleeps()