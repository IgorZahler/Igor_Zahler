#src/coop.py

import pygame
from src.tabuleiro import Tabuleiro

class CoopGame:
    def __init__(self, screen):
        self.screen = screen  # Armazena a tela
        self.tabuleiro = Tabuleiro(self.screen)  # Usa a tela para inicializar Tabuleiro
        self.jogador_atual = "X" # O jogador "X" começa
        self.state = "playing" # Mudar o estado do jogo para "jogando"
        self.ganhador = None # Nenhum vencedor ainda

    def troca_turno(self, row, col):
        # Verificar se o quadrado já foi ocupado
        if self.tabuleiro.marca_tabu[row][col] == "":
            # Jogador atual joga
            self.tabuleiro.marca_tabu[row][col] = self.jogador_atual

            # Verificar se tem um vencedor
            if self.verifica_ganhador(self.jogador_atual):
                self.ganhador = self.jogador_atual
                self.state = "game_over"
            else:
                # Troca de jogador
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verifica_ganhador(self, player):
        # Verifica linhas/colunas/diagonais
        for row in range(3):
            if all(self.tabuleiro.marca_tabu[row][col] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.tabuleiro.marca_tabu[row][col] == player for row in range(3)):
                return True
        if all(self.tabuleiro.marca_tabu[i][i] == player for i in range(3)):
            return True
        if all(self.tabuleiro.marca_tabu[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def update(self):
            # Aqui você pode adicionar a lógica para atualizar o estado do jogo, se necessário
            pass