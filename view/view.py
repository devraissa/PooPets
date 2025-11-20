from datetime import date
from models.dog import Dog

date = date.today().strftime('%d/%m/%Y')
pet = Dog(name="Django", satiety=0, health=50, happiness=50, rest=50, hygiene=50, sleep_cycles=4)

class View:
    def menu(self):
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

    def adoption_contract(self):
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
    
    def pet_status(self):
        return f"""\n╔════════════════════════════════════════════╗
║      ✨ MEU COMPANHEIRO: {pet.get_name} ✨                
╠════════════════════════════════════════════╣
║ 💗 SAÚDE: {pet.get_health} -> {"💚" if pet.get_health > 10 else "💔"}
║ 🍽️  SACIEDADE: {pet.get_satiety} -> {"✅" if pet.get_satiety > 10 else "❌"}
║ 🧼 HIGIENE: {pet.get_hygiene} -> {"🌸" if pet.get_hygiene > 10 else "🤢"}
║ 😊 FELICIDADE: {pet.get_happiness} -> {"🥳" if pet.get_happiness > 10 else "😭"}
║ 💤 DESCANSO: {pet.get_rest} -> {"🌙" if pet.get_rest > 10 else "😵"}
╚════════════════════════════════════════════╝"""
    
    def tombstone(self):
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