from ludo.token import Token
from ludo.constants import Color
class Player:
    color : Color
    tokens = []
    def __init__(self,color):
        self.color = color
        tokens=[
            Token(color),
            Token(color),
            Token(color),
            Token(color),
        ]
    


