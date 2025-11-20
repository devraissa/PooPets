class Pet:
    def __init__(self, name, satiety=50, health=100, hygiene=50, happiness=50, rest=100):
        self.__name = name
        self.__satiety = satiety
        self.__health = health
        self.__hygiene = hygiene
        self.__happiness = happiness
        self.__rest = rest

    # Manipular os valores dos atributos
    def set_satiety(self, value):
        return self.__satiety + (value)
    
    def set_health(self, value):
        return self.__health + (value)
    
    def set_hygiene(self, value):
        return self.__hygiene + (value)
    
    def set_happiness(self, value):
        return self.__happiness + (value)
    
    def set_rest(self, value):
        return self.__rest + (value)

    # Ações do Pet
    def feed_pet(self):
        return f"\nA barriguinha de {self.__name} está fazendo ron-ron! 🍼 Que delícia de rango!"
    
    def pet_plays(self):
        self.__satiety -= 20
        self.__health += 30
        self.__hygiene -= 20

        return f"\nCorre, {self.__name}! 🎉 A felicidade subiu no telhado! Agora é hora de tirar uma soneca, ops, quase!"

    def pet_takes_a_bath(self):
        self.__satiety -= 5
        self.__hygiene += 70
        self.__happiness += 10
        self.__health += 20
        self.__rest -= 5

        return f"\nCheirinho de bebê! ✨ {self.__name} se sacudiu, mas agora está um pinguinho de gente limpo!"

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
