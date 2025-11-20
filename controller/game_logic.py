import time
from utils import clear_terminal
from view.game_view import GameView
from models.dog import Dog
from models.cat import Cat
from models.bird import Bird

class Game:
    @staticmethod
    def pet_adoption_stage():
        """ Função que inicializa o jogo, mostra o menu com os animais disponíveis e o contrato de adoção com o nome do Pet. """
        pet = None

        try:
            # --- LOOP 1: Escolha da Espécie (Loop de Validação) ---
            while pet is None:
                print(GameView.menu())
                user_choice = input("\n->> ").upper()

                match user_choice:
                    case "1":
                        pet = Dog(name="", satiety=50, health=100, happiness=50, rest=50, hygiene=50, sleep_cycles=4)
                    case "2":
                        pet = Cat(name="", satiety=50, health=100, happiness=50, rest=50, hygiene=50, sleep_cycles=6)
                    case "3":
                        pet = Bird(name="", satiety=50, health=100, happiness=50, rest=50, hygiene=50, sleep_cycles=3)
                    case "S":
                        clear_terminal()
                        print(GameView.leaving_the_game())
                        return
                    case _:
                        clear_terminal()
                        print("🚨 Opção inválida! Voltando ao menu...")
                        return Game.pet_adoption_stage()

            # --- LOOP 2: Contrato e Nomeação (Validação do Nome) ---
            clear_terminal()
            print(GameView.adoption_contract())

            while True:
                pet_name = input("->> ").title().strip()

                if pet_name:
                    pet.set_name(pet_name)

                    print(f"\n🎉 Contrato assinado! Seu novo pet, {pet_name}, está pronto para ir para casa!")
                    
                    input("\nPressione ENTER para começar...")
                    return Game.pet_care(pet)
                else:
                    print("\n🚨 Nome inválido! Insira um nome válido para o seu pet.")

        except Exception as e:
            print(f"\nOcorreu um erro crítico: {e}")
            return
        
    @staticmethod
    def pet_care(pet):
        clear_terminal()
        try:
            print(GameView.care_instructions(pet))
            input("\nPressione ENTER para começar...")

            while True:
                clear_terminal()
                print(GameView.pet_status(pet))
                action = input(f"\nO que você fará por {pet.get_name}? ->> ").upper()

                Game.apply_critical_penalties(pet)

                if pet.get_health <= 0:
                    clear_terminal()
                    print(GameView.tombstone())
                    return False

                match action:
                    case "1":
                        input(pet.to_feed())
                    case "2":
                        input(pet.plays())
                    case "3":
                        input(pet.takes_a_bath())
                    case "4":
                        input(pet.receives_affection())
                    case "5":
                        print(pet.sleeps())

                        for hour in range(1, pet.get_sleep_cycles + 1):
                            time.sleep(1.5)
                            print(f"\n[{hour}/{pet.get_sleep_cycles}] Se passaram {hour} hora(s). Zzz...")

                        input(f"\n✨ {pet.get_name} acordou! Renovado(a) e pronto(a) para mais um dia!")
                        
                    case "S":
                        clear_terminal()
                        print(GameView.leaving_the_game())
                        return False
                    case _:
                        input("\n🚨 Opção inválida! Pressione ENTER para tentar novamente... ")
                continue

        except Exception as e:
            print(f"\nOcorreu um erro crítico> {e}")

    @staticmethod
    def apply_critical_penalties(pet):
        if pet.get_satiety <= 10:
            pet.set_health(value=(-20))

        if pet.get_hygiene <= 10:
            pet.set_health(value=(-5))
            pet.set_happiness(value=(-5))

        if pet.get_happiness <= 10:
            pet.set_health(value=(-20))

        if pet.get_rest <= 10:
            pet.set_health(value=(-40))
            pet.set_happiness(value=(-30))