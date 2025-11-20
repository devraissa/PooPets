class Pet:
    def __init__(self, satiety, health, hygiene, happiness, rest, sleep_cycles, name="Bichinho"):
        self.__name = name
        self.__sleep_cycles = sleep_cycles
        self.__satiety = self.__clamper_value(satiety)
        self.__health = self.__clamper_value(health)
        self.__hygiene = self.__clamper_value(hygiene)
        self.__happiness = self.__clamper_value(happiness)
        self.__rest = self.__clamper_value(rest)

    # FAZ O CONTROLE PARA QUE OS ATRIBUTOS NÃO ULTRAPASSEM DE 100 E NÃO SEJAM MENORES QUE 0.
    @staticmethod
    def __clamper_value(value):
        return max(0, min(100, value))

    # == EXIBE OS VALORES DO ATRIBUTOS | GETTERS ==
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_satiety(self):
        return self.__satiety
    
    @property
    def get_health(self):
        return self.__health
    
    @property
    def get_hygiene(self):
        return self.__hygiene
    
    @property
    def get_happiness(self):
        return self.__happiness
    
    @property
    def get_rest(self):
        return self.__rest

    # == MANIPULA OS VALORES DOS ATRIBUTOS | SETTERS ==
    def set_satiety(self, value):
        self.__satiety = self.__clamper_value(self.__satiety + value)
    
    def set_health(self, value):
        self.__health = self.__clamper_value(self.__health + value)
    
    def set_hygiene(self, value):
        self.__hygiene = self.__clamper_value(self.__hygiene + value)
    
    def set_happiness(self, value):
        self.__happiness = self.__clamper_value(self.__happiness + value)
    
    def set_rest(self, value):
        self.__rest = self.__clamper_value(self.__rest + value)

    # == AÇÕES DO PET ==
    def to_feed(self):
        return f"\nA barriguinha de {self.__name} está fazendo ron-ron! 🍼 Que delícia de rango!"
    
    def plays(self):
        self.set_satiety(value=(-20))
        self.set_health(value=30)
        self.set_hygiene(value=(-20))

        return f"\nCorre, {self.__name}! 🎉 A felicidade subiu no telhado! Agora é hora de tirar uma soneca, ops, quase!"

    def takes_a_bath(self):
        self.set_satiety(value=(-5))
        self.set_hygiene(value=70)
        self.set_happiness(value=10)
        self.set_health(value=20)
        self.set_rest(value=(-5))

        return f"\nCheirinho de bebê! ✨ {self.__name} se sacudiu, mas agora está um pinguinho de gente limpo!"

    def receives_affection(self):
        self.set_happiness(value=10)
        
        return f"\nAhhh... 💖 {self.__name} fechou os olhinhos e deu um suspiro de satisfação. A felicidade subiu rapidinho!"

    def sleeps(self):
        self.set_happiness(value=10)
        self.set_health(value=30)
        self.set_rest(value=100)
        
        return f"\nShhh... {self.__name} dormirá por {self.__sleep_cycles} horas. 😴 Ele voltará assim que as baterias estiverem cheias!"

    def makes_sound(self):
        pass
