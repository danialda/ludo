from enum import Enum
import pygame
class Color(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GRAY = (200, 200, 200)
    SKIN = (237, 193, 134)

class Player(Enum):
    blue = "Blue"
    green = "Green"
    yellow = "Yellow"
    red = "Red"

PlayerColor = {
Player.red.value : Color.RED.value,
Player.green.value : Color.GREEN.value,
Player.blue.value : Color.BLUE.value,
Player.yellow.value : Color.YELLOW.value
    }

WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 15

pygame.font.init() 
font = pygame.font.Font(None, 36) 

greenTokenIcon = pygame.image.load("assets/greenToken.png")
yellowTokenIcon = pygame.image.load("assets/yellowToken.png")
redTokenIcon = pygame.image.load("assets/redToken.png")
blueTokenIcon = pygame.image.load("assets/blueToken.png")
ludoIcon = pygame.image.load("assets/ludo.png")
# blueToken = pygame.image.load("assets/")
# EMPTY_SQUARE_IMG = pygame.transform.scale(pygame.image.load('assets/square gray dark _1x.png'), (SQUARE_SIZE, SQUARE_SIZE))

# PLAYER_RED_IMG = pygame.transform.scale(pygame.image.load('assets/player_red.png'), (SQUARE_SIZE * 0.9, SQUARE_SIZE * 0.9))
# PLAYER_RED_SELECTED_IMG = pygame.transform.scale(pygame.image.load('assets/player_red_selected.png'), (SQUARE_SIZE * 0.9, SQUARE_SIZE * 0.9))
# PLAYER_BLUE_IMG = pygame.transform.scale(pygame.image.load('assets/player_blue.png'), (SQUARE_SIZE * 0.9, SQUARE_SIZE * 0.9))
# PLAYER_BLUE_SELECTED_IMG = pygame.transform.scale(pygame.image.load('assets/player_blue_selected.png'), (SQUARE_SIZE * 0.9, SQUARE_SIZE * 0.9))




