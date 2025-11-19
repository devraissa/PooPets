🐶 Design de Jogo: PooPet

Este documento detalha o fluxo de jogo e a estrutura de Programação Orientada a Objetos (POO) do simulador de bichinho virtual "PooPet".

1. Estrutura e Fluxo do Jogo
O jogo opera em um loop contínuo no terminal (CLI), onde o objetivo principal é gerenciar os atributos de estado do Pet.
    1.1. Início e Adoção (Instanciação)
        - Execução: O arquivo principal (main.py) é o ponto de entrada.
        - Menu de Adoção: O usuário visualiza uma tabela listando os pets disponíveis para adoção (Ex: Cachorro, Gato, Pássaro) e seus atributos base
        - Criação do Objeto: Após a escolha do tipo de Pet e seu nome, uma instância (objeto) é criada. Essa instância pertence a uma classe filha que herda comportamentos e atributos da PetBase.

    1.2. Loop Principal (while True)
        O jogo prossegue em um ciclo infinito, onde a única forma de sair do loop é pelo comando Dormir (que deve ser refeito para ser a condição de Game Over ou salvar o jogo) ou pela morte do Pet.
            - Apresentação:
                - Exibe Nome e Status Atual do Pet.
                - Escolha uma ação: Alimentar, Brincar, Dar Banho, Passar o Tempo, ou Dormir.
            
            - Execução:
                - O método de instância é chamado (Ex: pet.alimentar()).
                
            - Verificação:
                - O sistema checa as Condições Críticas e aplica penalidades antes de prosseguir.
        
2. Estrutura POO e Atributos de Estado
Todos os atributos devem ser Encapsulados (usando self.__atributo) e manipulados exclusivamente por métodos. Os valores variam de 0 a 100.
    2.1. Atributos de Estado
        __saciedade  =  100 Satisfeito  /  0 Faminto
        __saude      =  100 Perfeita    /  0 Morte
        __higiene    =  100 Limpo       /  0 Sujo
        __felicidade =  100 Feliz       /  0 Triste
        __descanso   =  100 Acordado    /  0 Exausto
    
    2.2. Efeito dos Métodos de Ação
        alimentar ->  Saciedade += 20, Higiene -= 5, Felicidade += 5, Saúde += 20, Descanso -= 5
        dar_banho ->  Higiene += 70, Felicidade += 10, Saúde += 20, Descanso -= 5
        brincar   ->  Saciedade -= 20, Higiene -= 20, Felicidade += 40, Saúde += 30, Descanso -= 20
        carinho -> Felicidade += 10
        dormir    ->  Saciedade -= 10, Felicidade += 10, Saúde += 30, Descanso += 100 (reseta)

    2.3. Lógica de Passagem de Tempo (Sono Estratégico)
        O tempo no jogo (Decaimento Automático) só avança enquanto o pet está dormindo, exigindo planejamento prévio do jogador.
            1. Ação Dormir: Quando o usuário escolhe dormir(), o pet entra em um sub-loop de descanso.
            2. Ciclo de Decaimento: A cada ciclo do sub-loop, o método passar_tempo() é executado, aplicando decaimentos fixos:
                - Saciedade -= 5
                - Felicidade -= 5
            3. Verificação de Crise Durante o Sono: A cada ciclo, o sistema verifica se as condições críticas (Fome, Sujeira) causam a morte.
            4. Fim de Jogo: Se a Saúde atingir <= 0 durante o sono, o jogo encerra imediatamente. Caso contrário, o pet acorda ao final dos ciclos e o jogo retorna ao loop principal.
    
3. Condições Críticas e Fim de Jogo
    3.1. Penalidades por Status Crítico
        Saciedade <= 10    ->  Saúde -= 20 ao fazer qualquer ação exceto alimentar().
        Higiene <= 10      ->  Saúde -= 5 e Felicidade -= 5 ao fazer qualquer ação exceto dar_banho().
        Felicidade <= 10   ->  Saúde -= 20 a cada ação executada. Recusa comandos de Brincar e Dar Banho. Recusa Alimentar aleatoriamente.
        Descanso <= 10     ->  Saúde -= 40 e Felicidade -= 30 (por estar acordado). Recusa Alimentar, Brincar e Dar Banho.
    
    3.2. Fim de Jogo
        Condição: A simulação termina se o atributo __saude for <= 0.
        Mensagem: "{Nome do pet} está descansando para sempre..."
    
4. Diferenciação por Espécie (Polimorfismo)
    As subclasses (Cachorro, Gato, Pássaro) devem implementar o conceito de Polimorfismo através de:
        - Métodos Únicos: Como o emitir_som(), que retorna uma string diferente para cada espécie.
        - Variação de Lógica: Ajustar os valores de aumento/diminuição nos métodos de ação (Ex: Cachorro.brincar() aumenta Felicidade mais rápido que Gato.brincar()).