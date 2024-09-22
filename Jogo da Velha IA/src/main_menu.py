# src/main_menu.py
import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("src/background.png")
        self.font = pygame.font.Font(None, 74)
        self.menu_options = ["Jogo Solo", "Jogo Coop", "Sair"]
        self.selected_option = 0
        
    def draw(self):
        # Desenhar o fundo
        self.screen.blit(self.background, (0, 0))

        # Desenhar o título do jogo
        title_text = self.font.render("JOGO DA VELHA", True, (255, 255, 255))
        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 100))

        # Desenhar as opções do menu
        for i, option in enumerate(self.menu_options):
            color = (255, 255, 255) if i == self.selected_option else (100, 100, 100)
            option_text = self.font.render(option, True, color)
            self.screen.blit(option_text, (self.screen.get_width() // 2 - option_text.get_width() // 2, 250 + i * 100))

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                elif event.key == pygame.K_RETURN:
                    if self.menu_options[self.selected_option] == "Jogo Solo":
                        return "start_solo_game"
                    elif self.menu_options[self.selected_option] == "Jogo Coop":
                        return "start_coop_game"
                    elif self.menu_options[self.selected_option] == "Sair":
                        pygame.quit()
                        exit()
        return None
