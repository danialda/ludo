
from ludo.constants import plyer

class State:
    blueTokens = [-1,-1,-1,-1]
    greenTokens = [-1,-1,-1,-1]
    def __init__(self):
        self.parent=None   
        self.cost = 0
