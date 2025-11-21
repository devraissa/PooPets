import time
from utils import clear_terminal
from view.game_view import GameView
from models.dog import Dog
from models.cat import Cat
from models.bird import Bird

class Game:
    """ Controlador principal do jogo PooPet. Gerencia o fluxo de fases (Adoção, Cuidado) e a lógica de penalidades. Todos os métodos são estáticos (@staticmethod) pois manipulam o estado do jogo através do objeto 'pet' passado como argumento. """

    @staticmethod
    def pet_adoption_stage():
        """ Inicializa o jogo, lida com a seleção da espécie e valida a nomeação. Retorna o objeto Pet instanciado para o loop principal. """
        pet = None

        try:
            # --- LOOP 1: Escolha da Espécie (Loop de Validação) --- O loop continua até que o Pet seja instanciado ou o usuário saia.
            while pet is None:
                print(GameView.menu())
                user_choice = input("\n->> ").upper()

                # Usa match/case para instanciar a classe Pet correta
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
            print(GameView.adoption_contract()) # Exibe o contrato

            while True:
                pet_name = input("->> ").title().strip()

                if pet_name: # Nome válido: atribui e prossegue
                    pet.set_name(pet_name)

                    # Mensagem de sucesso e transição
                    print(f"\n🎉 Contrato assinado! Seu novo pet, {pet_name}, está pronto para ir para casa!")
                    
                    input("\nPressione ENTER para começar...")
                    # Chama o loop principal do jogo, passando o objeto Pet instanciado
                    return Game.pet_care(pet)
                else:
                    print("\n🚨 Nome inválido! Insira um nome válido para o seu pet.")

        except Exception as e:
            print(f"\nOcorreu um erro crítico: {e}")
            return
        
    @staticmethod
    def pet_care(pet):
        """ Contém o loop principal de cuidado do jogo. """
        clear_terminal()
        try:
            # Exibe as instruções iniciais usando o nome do pet
            print(GameView.care_instructions(pet))
            input("\nPressione ENTER para começar...")

            while True:
                clear_terminal()

                # PASSO 1: Exibir Status e Menu de Ações
                print(GameView.pet_status(pet))

                # Armazenamos a ação para passar ao sistema de penalidades
                action = input(f"\nO que você fará por {pet.get_name}? ->> ").upper()

                # PASSO 2: Execução da Ação
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
                        # Ação de dormir (inicia o sub-loop de tempo)
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

                # PASSO 3: Aplicar Penalidades Críticas antes da ação
                Game.apply_critical_penalties(pet)

                # PASSO 4: Checagem de Morte
                if pet.get_health <= 0:
                    clear_terminal()
                    print(GameView.tombstone())
                    return False

        except Exception as e:
            print(f"\nOcorreu um erro crítico> {e}")

    @staticmethod
    def apply_critical_penalties(pet):
        """ Verifica os limites críticos de Saciedade, Higiene, Felicidade e Descanso e aplica o decaimento correspondente na Saúde do Pet. """

        # --- 1. Fome Extrema (Saciedade <= 10) ---
        # Penalidade só é aplicada se a última ação NÃO foi alimentar.
        if pet.get_satiety <= 10:
            pet.set_health(value=(-20))

        # --- 2. Sujeira Extrema (Higiene <= 10) ---
        # Penalidade só é aplicada se a última ação NÃO foi banho.
        if pet.get_hygiene <= 10:
            pet.set_health(value=(-5))
            pet.set_happiness(value=(-5))

        # --- 3. Tristeza Profunda (Felicidade <= 10) ---
        if pet.get_happiness <= 10:
            pet.set_health(value=(-20))

        # --- 4. Exaustão (Descanso <= 10) ---
        if pet.get_rest <= 10:
            pet.set_health(value=(-40))
            pet.set_happiness(value=(-30))