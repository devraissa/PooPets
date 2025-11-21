# 🐶 PooPet – Seu Companheiro Virtual em Python! 🐾

**“A maneira mais fofa de dominar a Programação Orientada a Objetos.”**

PooPet é um jogo de pet virtual rodando em **CLI (terminal)** desenvolvido em **Python**, com foco total na prática e consolidação de **Programação Orientada a Objetos (POO)**.
Inspirado em clássicos como Tamagotchi, seu objetivo é cuidar de um pet digital (Cachorro, Gato ou Pássaro), mantendo seus atributos vitais em equilíbrio.

Se o pet for negligenciado, penalidades são acumuladas e, eventualmente… ele pode morrer. 😢

---

## ✨ Objetivo do Projeto

Este projeto foi criado para reforçar os principais pilares da POO, de forma prática, limpa e divertida.

Os conceitos aplicados incluem:

| Conceito               | Aplicação no Projeto                                                                                                 |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Encapsulamento**     | Atributos como `__satiety`, `__health`, etc., são privados e manipulados apenas via getters e setters.               |
| **Segurança de dados** | O método interno `__clamper_value` garante que os valores de atributos estejam sempre entre 0 e 100.                 |
| **Herança**            | A classe `Pet` define toda a base de comportamento. As classes `Dog`, `Cat` e `Bird` herdam essa estrutura.          |
| **Polimorfismo**       | Métodos como `plays()` e `sleeps()` são sobrescritos em cada espécie para simular diferenças reais entre os animais. |

---

## 🚀 Como Jogar

### 📌 Pré-requisitos

* Python **3.x** instalado no sistema.

### 📥 Instalação e Execução

1. Clone o repositório:

2. Acesse a pasta raiz:

3. Execute o jogo:

```
python main.py
```

### 🎮 Gameplay

* **Adoção**
  Escolha seu pet e assine o Termo de Adoção (com arte ASCII!).

* **Cuidados**
  Gerencie atributos como:

  * Saciedade
  * Saúde
  * Higiene
  * Felicidade
  * Descanso

* **Riscos**
  Baixos níveis de Saciedade ou Descanso geram penalidades severas e podem reduzir drasticamente a Saúde.

* **Sono estratégico**
  A função de dormir simula passagem de tempo com `time.sleep()`.
  Planeje bem antes de deixar seu pet descansar!

---

## 🛠️ Arquitetura do Projeto

A organização segue princípios limpos de Model–View–Controller:

```
POOPET/
├── controller/
│   └── game_logic.py      → Classe Game (controlador central)
├── view/
│   └── game_view.py       → Classe GameView (ASCII Art, menus e interface)
│── models/
│    ├── pet.py             → Classe base Pet
│    ├── dog.py             → Classe Dog
│    ├── cat.py             → Classe Cat
│    └── bird.py            → Classe Bird
├── main.py
└── utils.py 

```

### Responsabilidades

* **Modelos (`models/`)**
  Guardam dados e lógicas específicas (ações polimórficas).

* **View (`view/`)**
  Exibe menus, status, telas e artes em ASCII.

* **Controller (`controller/`)**
  Gerencia o fluxo do jogo e regras crítico-lógicas como penalizações.

---

## 🌟 Espécies e Comportamentos

Cada pet tem um conjunto único de características, aplicadas via **polimorfismo**:

| Espécie     | Comportamento                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------ |
| 🐶 Cachorro | Muito ativo. Ganha muita Felicidade ao brincar, mas perde muito Descanso e fica com mais fome.   |
| 🐱 Gato     | Comportamento mais calmo. Gasta pouco Descanso e Saciedade, metabolism lento.                    |
| 🐦 Pássaro  | Metabolismo acelerado: perde muito Descanso e Saciedade rapidamente, mas ganha muita Felicidade. |

---

## 🧠 Aprendizados

Este projeto ensina, na prática:

* Encapsulamento profissional com `@property`
* Herança e reutilização de código
* Polimorfismo real aplicado em lógica de jogo
* UI de terminal com ASCII Art
* Organização modular em Python
* Controle de estado e ciclo de vida

---

## 💛 Obrigado por Jogar!

Cuide bem do seu companheiro virtual…
ou o pior pode acontecer! ⚠️

Boa diversão e bom código! 🎮🐾
