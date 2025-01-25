import pygame
from ludo.constants import WIDTH,HEIGHT,Color , TWO_PLAYER_BUTTON_DIM , FOUR_PLAYER_BUTTON_DIM, EXIT_DIM,TWO_PLAYER_FONT_DIM,FOUR_PLAYER_FONT_DIM,EXIT_FONT_DIM,ludoBackGround

def SelectNumOfPlayers(WIN):
    pygame.font.init()  # Initialize the font module
    pygame.mixer.init()  # Initialize the mixer module

    menu_run = True
    hovered_button = None  # To track the currently hovered button

    hover_blue = (0, 0, 255)
    hover_red = (255, 0, 0)
    hover_grey = (100, 100, 100)
    img = ludoBackGround
    scaled_img = pygame.transform.scale(img, (WIDTH, HEIGHT))
    while menu_run:
        WIN.blit(scaled_img, (0, 0))

        # Define buttons
        two_player_button = pygame.Rect(TWO_PLAYER_BUTTON_DIM)
        four_player_button = pygame.Rect(FOUR_PLAYER_BUTTON_DIM)
        exit_button = pygame.Rect(EXIT_DIM)

        mouse_pos = pygame.mouse.get_pos()

        # Detect hover for each button and play sound once
        for button, color, hover_color, label, font_dim in [
            (two_player_button, Color.BLUE.value, hover_blue, "Two Players", TWO_PLAYER_FONT_DIM),
            (four_player_button, Color.RED.value, hover_red, "Four Players", FOUR_PLAYER_FONT_DIM),
            (exit_button, Color.GRAY.value, hover_grey, "Exit", EXIT_FONT_DIM),
        ]:
            if button.collidepoint(mouse_pos):
                pygame.draw.rect(WIN, hover_color, button.inflate(10, 10))
                if hovered_button != button:
                    # HOVER_SOUND.play()
                    hovered_button = button  # Update hovered button
            else:
                pygame.draw.rect(WIN, color, button)

        # Render text
        font = pygame.font.Font(None, 40)
        WIN.blit(font.render("Two Players", True, Color.WHITE.value), TWO_PLAYER_FONT_DIM)
        WIN.blit(font.render("Four Players", True, Color.WHITE.value), FOUR_PLAYER_FONT_DIM)
        WIN.blit(font.render("Exit", True, Color.WHITE.value), EXIT_FONT_DIM)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if two_player_button.collidepoint(pos):
                    return 2
                elif four_player_button.collidepoint(pos):
                    return 4
                elif exit_button.collidepoint(pos):
                    pygame.quit()
                    exit()