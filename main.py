import pygame
import sys
from ludo.game_structure import GameStructure

def main():
    clock = pygame.time.Clock()
    game = GameStructure()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.draw_board()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()