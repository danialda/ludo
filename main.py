import pygame
from ludo.constants import WIDTH, HEIGHT


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob Wars')


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # row, col = get_row_col_from_mouse(pos)
                # game.select(row, col)
                # game.update()

    pygame.quit()
main()
