# src/game.py
import pygame
from src.main_menu import MainMenu
from src.coop import CoopGame  

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = "menu"  # Estado inicial como menu
        self.main_menu = MainMenu(screen)
        self.player = None
        self.Ia = None
        self.boss = None
        self.coop_game = None  # Inicializa a variável coop_game

    def start_coop_game(self):
        self.coop_game = CoopGame(self.screen)  # Cria uma nova instância de CoopGame
        self.state = "playing"  # Muda o estado para "jogando"

    def draw(self):
        if self.state == "menu":
            self.main_menu.draw()
        elif self.state == "playing":
            self.screen.fill((0, 0, 0))
            if self.coop_game:
                # Se tiver uma instância de CoopGame, desenhe o tabuleiro
                self.coop_game.tabuleiro.desenhar_tabu()  # Chama o método de desenhar o tabuleiro

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if self.state == "menu":
            action = self.main_menu.update(events)
            if action == "start_solo_game":
                self.start_solo_game()
            elif action == "start_coop_game":
                self.start_coop_game()  # Carrega o jogo Coop
            elif action == "exit":
                pygame.quit()
                exit()
        elif self.state == "playing":
            if self.coop_game:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        self.coop_game.tabuleiro.testa_pos(mouse_pos)  # Verifica se o clique foi em uma posição válida
                self.coop_game.update()  # Chama o método de update na instância de CoopGame

    def run(self):
        while True:
            self.update()  # Atualiza o estado do jogo
            self.draw()    # Desenha na tela
            pygame.display.flip()  # Atualiza a tela
