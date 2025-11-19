class Pet:
    def __init__(self, name, satiety, health, hygiene, happiness, rest):
        self.__name = name
        self.__satiety = satiety
        self.__health = health
        self.__hygiene = hygiene
        self.__happiness = happiness
        self.__rest = rest

    @property
    def name(self):
        return self.__name
    
    @property
    def satiety(self):
        return self.__satiety
    
    @property
    def health(self):
        return self.__health
    
    @property
    def hygiene(self):
        return self.__hygiene
    
    @property
    def happiness(self):
        return self.__happiness
    
    @property
    def rest(self):
        return self.__rest
    
    def feed_pet(self):
        return f"\nA barriguinha de {self.__name} está fazendo ron-ron! 🍼 Que delícia de rango!"

    def pet_plays(self):
        return f"\nCorre, {self.__name}! 🎉 A felicidade subiu no telhado! Agora é hora de tirar uma soneca, ops, quase!"

    def pet_takes_a_bath(self):
        self.__hygiene += 70
        self.__happiness += 10
        self.__health += 20
        self.__rest -= 5

        return f"\nCheirinho de bebê! ✨ {self.name} se sacudiu, mas agora está um pinguinho de gente limpo!"
        pass

    def pet_receives_affection(self):
        self.__happiness += 10
        
        return f"\nAhhh... 💖 {self.__name} fechou os olhinhos e deu um suspiro de satisfação. A felicidade subiu rapidinho!"

    def pet_sleeps(self):
        self.__happiness += 10
        self.__health += 30
        self.__rest = 100
        
        return f"\nShhh... {self.__name} está contando carneirinhos. 😴 Ele voltará assim que as baterias estiverem cheias!"

    def pet_makes_sound(self):
        pass
