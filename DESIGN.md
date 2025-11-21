# 🐶 Design do Jogo: PooPet

Este documento detalha o fluxo de jogo e a estrutura de Programação Orientada a Objetos (POO) do simulador de bichinho virtual "PooPet". Ele reflete a implementação final dos módulos Game, GameView e as classes de Models.

## 🧠 Foco POO do Projeto

O projeto foi construído sobre os seguintes pilares, garantindo modularidade e segurança:

Encapsulamento: Todos os atributos (__satiety, __health, etc.) são privados e manipulados exclusivamente por métodos Setters dedicados.

Segurança de Dados (Clamping): O método estático __clamper_value garante que todos os atributos numéricos permaneçam rigorosamente entre 0 e 100.

Herança: As subclasses (Dog, Cat, Bird) herdam a lógica base de cuidados da classe mãe (Pet).

Polimorfismo: As subclasses sobrescrevem as ações (plays, to_feed, sleeps) para aplicar impactos e valores específicos de cada espécie, refletindo seu metabolismo e comportamento.


### 1. Estrutura e Fluxo do Jogo
    O jogo opera em um loop contínuo no terminal (CLI), controlado pela classe Game.

        1.1. Início e Adoção (Classe Game.pet_adoption_stage)
            Execução -> O arquivo principal (main.py) chama o método Game.pet_adoption_stage().

            Menu de Adoção -> O usuário visualiza o menu de espécies em um loop de validação (sem recursão).

            Criação do Objeto -> Após a escolha, a instância da classe filha (ex: Dog) é criada.

            Contrato -> O usuário é levado ao Termo de Adoção, onde o nome do Pet é coletado e validado.

            Transição -> O objeto Pet instanciado e nomeado é retornado para a fase de cuidados (Game.pet_care).

        1.2. Loop Principal (Método Game.pet_care)

        O jogo prossegue em um ciclo infinito (while True). A principal lógica de risco reside na ordem de execução.
            Status -> Limpa a tela e exibe o painel de status (GameView.pet_status) e o menu de ações. -> GameView

            Ação -> O match/case executa o método de instância do Pet (ex: pet.plays()). -> Pet/Subclasses

            Decaimento/Penalidade -> O método Game.apply_critical_penalties(pet, acao) é chamado para verificar se o Pet entrou em estado crítico e penalizar a Saúde. -> Game

            Fim de Jogo -> A verificação final (if pet.get_health <= 0) exibe a Lápide (GameView.tombstone) e encerra o programa. -> Game


### 2. Estrutura POO e Atributos de Estado

    Todos os atributos são encapsulados e manipulados exclusivamente através de Setters que invocam o __clamper_value (limite 0-100).

    2.1. Atributos de Estado (Lógica 100=Bom, 0=Ruim)
        __saciedade -> Satisfeito -> Fome Extrema -> Menor ou Igual a 10

        __saude -> Perfeita -> Morte -> Menor ou Igual a 0

        __higiene -> Limpo -> Sujeira Extrema -> Menor ou Igual a 10

        __felicidade -> Feliz -> Tristeza Profunda -> Menor ou Igual a 10

        __descanso -> Energético -> Exaustão -> Menor ou Igual a 10

    2.2. Efeito dos Métodos de Ação (Ajustado ao Código)
        O método da subclasse aplica o valor específico e depois chama super().metodo() para aplicar os valores base de bônus e perdas universais.

            to_feed() -> Saciedade Aumenta 20, Higiene Diminui 5, Felicidade Aumenta 5, Saúde Aumenta 20, Descanso Diminui 5 -> Passarinho: Saciedade Aumenta 15

            takes_a_bath() -> Higiene Aumenta 70, Felicidade Aumenta 10, Saúde Aumenta 20, Descanso Diminui 5, Saciedade Diminui 5 -> N/A (Lógica Universal)

            plays() -> Saciedade Diminui 20, Higiene Diminui 20, Saúde Aumenta 30 -> Cachorro: Felicidade Aumenta 60, Descanso Diminui 30

            receives_affection() -> Felicidade Aumenta 10 -> N/A (Lógica Universal)

            sleeps() -> Felicidade Aumenta 10, Saúde Aumenta 30, Descanso Aumenta 100 (reseta) -> Passarinho: Saciedade Diminui 12 (Perda inicial)

    2.3. Lógica de Passagem de Tempo (Sono Estratégico)
        O método Game.iniciar_sono_estrategico contém um sub-loop com time.sleep(1.5) para simular a passagem de tempo.

        Ciclo de Decaimento (por hora): Saciedade Diminui (valor polimórfico), Felicidade Diminui 5, Higiene Diminui 1.

        Verificação: O método Game.apply_critical_penalties é chamado a cada ciclo do sono para checar a morte por fome/sujeira.


### 3. Condições Críticas e Penalidades

    3.1. Método de Controle (Game.apply_critical_penalties)
        Este método, chamado após cada ação no pet_care, verifica as condições críticas (<= 10) e aplica o impacto na Saúde e Felicidade.

            Exaustão -> Descanso Menor ou Igual a 10 -> Saúde Diminui 40, Felicidade Diminui 30 -> N/A

            Fome Extrema -> Saciedade Menor ou Igual a 10 -> Saúde Diminui 20 -> Se a última ação foi Alimentar

            Sujeira Extrema -> Higiene Menor ou Igual a 10 -> Saúde Diminui 5, Felicidade Diminui 5 -> Se a última ação foi Dar Banho

            Tristeza Profunda -> Felicidade Menor ou Igual a 10 -> Saúde Diminui 20 -> N/A

    3.2. Fim de Jogo
        Condição: A simulação termina se pet.get_health() for Menor ou Igual a 0.

        Mensagem: Exibe a tela de "Lápide" (GameView.tombstone) e a mensagem de reflexão.