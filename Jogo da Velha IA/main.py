# main.py
import pygame
from src.game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("JOGO DA VELHA")
    clock = pygame.time.Clock()
    
    game = Game(screen)

    running = True
    while running:
        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()