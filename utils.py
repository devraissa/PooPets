import os

def clear_terminal():
    """ Função auxiliar para limpar a tela do terminal. """
    os.system('cls' if os.name == 'nt' else 'clear')