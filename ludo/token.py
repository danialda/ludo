from constants import Color,TokenStatus
class Token:
    color : Color
    row = -1
    col = -1
    status = TokenStatus.InHome
    def __init__(self,color):
        self.color = color
