from datetime import date

date = date.today().strftime('%d/%m/%Y')

class GameView:
    @staticmethod
    def menu():
        return """\n+---------------------------------------------------+
|                 🦴 ** POOPETS ** 🦴               |
|        Onde seu novo melhor amigo te espera!      |
+---------------------------------------------------+
|  /ᐠ｡ꞈ｡ᐟ\   /ᐠ｡ꞈ｡ᐟ\   /ᐠ｡ꞈ｡ᐟ\   /ᐠ｡ꞈ｡ᐟ\   /ᐠ｡ꞈ｡ᐟ\  |
|                                                   |
|            ✨ Escolha seu Companheiro ✨          |
|                                                   |
|  [1] Cachorro 🐕  [2] Gato 🐈  [3] Passarinho 🐦  |
|    (Lambeijos)     (Ronrons)      (Cacarecos)     |
|                                                   |
|         🐾 Qual patinha você escolhe? 🐾          |
+---------------------------------------------------+
|  [S] Sair e dar tchau...                          |
+---------------------------------------------------+"""

    @staticmethod
    def leaving_the_game():
        return f"""╔═════════════════════════════════════════════════════════════╗
║                                                             ║
║                  💖 ATÉ LOGO, CUIDADOR(A)! 💖               ║
║                                                             ║
║  Obrigado por dedicar seu tempo ao PooPet.                  ║
║  Esperamos que você volte logo, pois seus amigos virtuais   ║
║  sentirão saudades e estarão esperando por mais carinho!    ║
║                                                             ║
║  ⚠️ IMPORTANTE: Tudo o que aconteceu nesta sessão será       ║
║  apagado. Prepare-se para uma nova aventura na próxima vez! ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝"""

    @staticmethod
    def care_instructions(pet):
        return f"""\n╔═════════════════════════════════════════════════════════════╗
║                                                             ║
║     🐾 SUA AVENTURA COMO GUARDIÃO(Ã) COMEÇA AGORA! 🐾       ║
║                                                             ║
║     Fique de olho no painel de STATUS do seu pet.           ║
║     Cada ação que você toma (Brincar, Alimentar, etc.)      ║
║     afeta o equilíbrio da vida dele.                        ║
║                                                             ║
║     Lembre-se das métricas vitais:                          ║
║     ✨ Mantenha a Saciedade, Higiene e Felicidade altas!    ║
║     🚨 Se a Saúde (💗) chegar a ZERO, o jogo acaba!         ║
║                                                             ║
║     Tudo pronto? Seja o melhor amigo que {pet.get_name} pode ter!     ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝"""

    @staticmethod
    def adoption_contract():
        return f"""\n+---------------------------------------------------+
|               📝 CONTRATO DE ADOÇÃO 📝            |
|         VOCÊ ACEITA SER O HUMANO DESTE PET?       |
+---------------------------------------------------+
|                                                   |
| Eu, Cuidador(a), me comprometo a cuidar com amor  |
| e responsabilidade do meu novo companheiro.       |
|                                                   |
| A partir de agora, o pet:                         |
|                                                   |
| Nome do Pet: ___________________________________  |
|                                                   |
| passará a ser minha prioridade, garantindo que    |
| suas necessidades de SAÚDE, SACIEDADE, HIGIENE,   |
| FELICIDADE e DESCANSO sejam sempre atendidas.     |
|                                                   |
| Data: {date}                                  |
| Assinatura do Guardião(ã): 𝓒𝓾𝓲𝓭𝓪𝓭𝓸𝓻(𝓪)            |
+---------------------------------------------------+
| Digite o nome escolhido para finalizar o contrato:|
+---------------------------------------------------+"""
    
    @staticmethod
    def pet_status(pet):
        return f"""\n╔════════════════════════════════════════════╗
║      ✨ MEU COMPANHEIRO: {pet.get_name:5} ✨          ║
╠════════════════════════════════════════════╣
║ 💗 SAÚDE: {pet.get_health:3} -> {"💚" if pet.get_health > 10 else "💔"}                        ║
║ 🍽️  SACIEDADE: {pet.get_satiety:3} -> {"✅" if pet.get_satiety > 10 else "❌"}                    ║
║ 🧼 HIGIENE: {pet.get_hygiene:3} -> {"🌸" if pet.get_hygiene > 10 else "🤢"}                      ║
║ 😊 FELICIDADE: {pet.get_happiness:3} -> {"🥳" if pet.get_happiness > 10 else "😭"}                   ║
║ 💤 DESCANSO: {pet.get_rest:3} -> {"🌙" if pet.get_rest > 10 else "😵"}                     ║
╚════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════════════╗
║                       MENU DE AÇÕES                         ║
╠═════════════════════════════════════════════════════════════╣
║ [1] ALIMENTAR 🍽️  |  [2] BRINCAR ⚽  |  [3] DAR BANHO 🛀     ║
║ ----------------------------------------------------------- ║
║ [4] CARINHO 💖    |  [5] DORMIR 💤   |  [S] SAIR DO JOGO 👋 ║
╚═════════════════════════════════════════════════════════════╝"""
    
    @staticmethod
    def tombstone():
        return f"""+-------------------------------------------------------------+
|                                                             |
|                   😭  FIM DE JOGO  😭                       |
|                                                             |
+═════════════════════════════════════════════════════════════+
|                  DESCANSO ETERNO                            |
|                                                             |
|        ╔═══════════════════════════════════════════╗        |
|        ║           NOSSO AMOR VIVE AQUI            ║        |
|        ║                                           ║        |
|        ║                AQUI JAZ:                  ║        |
|        ║  Uma vida que não foi amada como deveria  ║        |
|        ║                                           ║        |
|        ║  Seu pequeno coração parou de pulsar...   ║        |
|        ╚═══════════════════════════════════════════╝        |
|                                                             |
|                                                             |
| Você assumiu a missão de cuidar de uma vida, mas infelizmen-|
| te o Amor, a Saúde e a Atenção não foram suficientes.       |
|                                                             |
| Seu pet dependia de você para manter o equilíbrio, e agora  |
| ele se foi por falta dos cuidados necessários.              |
|                                                             |
| Não desanime! A falha faz parte do aprendizado.             |
|                                                             |
| Tente Mais na Próxima Vez! Um novo pet espera por você!     |
|                                                             |
+-------------------------------------------------------------+"""