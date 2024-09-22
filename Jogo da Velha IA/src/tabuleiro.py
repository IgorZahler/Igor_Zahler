# src/tabuleiro.py

import pygame
from pygame.locals import MOUSEBUTTONDOWN, Rect

class Tabuleiro:
    def __init__(self, screen):
        self.screen = screen
        self.ESTADO = 'JOGANDO'
        self.VEZ = 'JOGADOR1'
        self.ESCOLHA = 'X'
        self.espaco = 0
        self.marca_tabu = [None] * 9  # Inicializa com None
        
        # Retângulos para cada posição do tabuleiro
        self.rects = [Rect((i % 3 * 200, i // 3 * 200), (200, 200)) for i in range(9)]

    def desenhar_tabu(self):
        # Desenha linhas do tabuleiro
        for i in range(3):
            pygame.draw.line(self.screen, (255, 255, 255), (i * 200, 0), (i * 200, 600), 10)
        for i in range(3):
            pygame.draw.line(self.screen, (255, 255, 255), (0, i * 200), (600, i * 200), 10)

        # Desenhar jogadas no tabuleiro
        for i, mark in enumerate(self.marca_tabu):
            x = (i % 3) * 200 + 100
            y = (i // 3) * 200 + 100
            if mark == "X":
                pygame.draw.line(self.screen, (255, 0, 0), (x - 50, y - 50), (x + 50, y + 50), 10)
                pygame.draw.line(self.screen, (255, 0, 0), (x + 50, y - 50), (x - 50, y + 50), 10)
            elif mark == "O":
                pygame.draw.circle(self.screen, (0, 0, 255), (x, y), 50, 10)

    def testa_pos(self, mouse_pos):
        for i, rect in enumerate(self.rects):
            if rect.collidepoint(mouse_pos) and self.marca_tabu[i] is None:
                self.confimar(i)
                break

    def confimar(self, indice):
        self.marca_tabu[indice] = self.ESCOLHA
        self.espaco += 1
        self.VEZ = 'JOGADOR2' if self.VEZ == 'JOGADOR1' else 'JOGADOR1'
        self.ESCOLHA = 'X' if self.VEZ == 'JOGADOR1' else 'O'

    def teste_vitoria(self, l):
        return any(all(self.marca_tabu[i] == l for i in combo) for combo in (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ))

    def reset(self):
        self.ESTADO = 'JOGANDO'
        self.VEZ = 'JOGADOR1'
        self.ESCOLHA = 'X'
        self.espaco = 0
        self.marca_tabu = [None] * 9
