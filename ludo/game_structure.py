import pygame
from ludo.constants import WIDTH , HEIGHT , CELL_SIZE , Color 
class GameStructure:
    pygame.init()
    
    shiftBetweenCirlcesInHome = 0.55 

    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ludo Game")
    
    def draw_board(self):
        self.screen.fill(Color.WHITE.value)
        
        for row in range(15):
            for col in range(15):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                self.colortheCellIfPath(row,col)
                pygame.draw.rect(self.screen, Color.BLACK.value, (x, y, CELL_SIZE, CELL_SIZE), 1)
        # Draw the center square
        self.drawCenter()

        # Draw home areas
        pygame.draw.rect(self.screen, Color.SKIN.value , (0, 0, CELL_SIZE * 6, CELL_SIZE * 6))  
        pygame.draw.rect(self.screen, Color.SKIN.value , (CELL_SIZE * 9, 0, CELL_SIZE * 6, CELL_SIZE * 6))  
        pygame.draw.rect(self.screen, Color.SKIN.value , (0, CELL_SIZE * 9, CELL_SIZE * 6, CELL_SIZE * 6))  
        pygame.draw.rect(self.screen, Color.SKIN.value , (CELL_SIZE * 9, CELL_SIZE * 9, CELL_SIZE * 6, CELL_SIZE * 6))  
        
        self.drawCircleWithBoard(CELL_SIZE * (3/2),Color.BLUE.value,3,3)
        self.drawInnerCircles(3,3)
        self.drawCircleWithBoard(CELL_SIZE * (3/2),Color.RED.value,12,3)
        self.drawInnerCircles(12,3)
        self.drawCircleWithBoard(CELL_SIZE * (3/2),Color.YELLOW.value,3,12)
        self.drawInnerCircles(3,12)
        self.drawCircleWithBoard(CELL_SIZE * (3/2),Color.GREEN.value,12,12)
        self.drawInnerCircles(12,12)

    def draw_Token(self , color , row , col):
        pygame.draw.circle(self.screen, Color.BLACK.value, ((CELL_SIZE*col) + (CELL_SIZE/2), (CELL_SIZE*row) + (CELL_SIZE/2)), CELL_SIZE // 3)
        pygame.draw.circle(self.screen, color, ((CELL_SIZE*col) + (CELL_SIZE/2), (CELL_SIZE*row) + (CELL_SIZE/2)), CELL_SIZE // 3 -1)


    def drawInnerCircles(self , widthCenter , hightCenter ):
        shiftValue = self.shiftBetweenCirlcesInHome

        self.drawCircleWithBoard(CELL_SIZE // 2, Color.WHITE.value, widthCenter-shiftValue, hightCenter-shiftValue)
        self.drawCircleWithBoard(CELL_SIZE // 2, Color.WHITE.value, widthCenter-shiftValue, hightCenter+shiftValue)
        self.drawCircleWithBoard(CELL_SIZE // 2, Color.WHITE.value, widthCenter+shiftValue, hightCenter-shiftValue)
        self.drawCircleWithBoard(CELL_SIZE // 2, Color.WHITE.value, widthCenter+shiftValue, hightCenter+shiftValue)
        
    def drawCircleWithBoard(self, radius, color:Color, widthCenter , hightCenter):
        bordWidth = 1 
        pygame.draw.circle(self.screen, Color.BLACK.value, (CELL_SIZE * widthCenter, CELL_SIZE * hightCenter), radius)
        pygame.draw.circle(self.screen, color, (CELL_SIZE * widthCenter, CELL_SIZE * hightCenter), radius - bordWidth)
    
    def drawCenter(self): 
        pygame.draw.polygon(
            self.screen,Color.RED.value ,
            [
            (CELL_SIZE * 6, CELL_SIZE * 6),
            (CELL_SIZE * 9, CELL_SIZE * 6),
            (CELL_SIZE * 7.5, CELL_SIZE * 7.5),
        ])
        pygame.draw.polygon(
            self.screen,Color.GREEN.value ,
            [
            (CELL_SIZE * 9, CELL_SIZE * 6),
            (CELL_SIZE * 9, CELL_SIZE * 9),
            (CELL_SIZE * 7.5, CELL_SIZE * 7.5),
        ])
        pygame.draw.polygon(
            self.screen,Color.YELLOW.value ,
            [
            (CELL_SIZE * 9, CELL_SIZE * 9),
            (CELL_SIZE * 6, CELL_SIZE * 9),
            (CELL_SIZE * 7.5, CELL_SIZE * 7.5),
        ])
        pygame.draw.polygon(
            self.screen,Color.BLUE.value ,
            [
            (CELL_SIZE * 6, CELL_SIZE * 9),
            (CELL_SIZE * 6, CELL_SIZE * 6),
            (CELL_SIZE * 7.5, CELL_SIZE * 7.5),
        ])

    def colortheCellIfPath(self,row,col):
        if((row > 0 and row < 6 and col == 7) or (col == 8 and row == 1)):
            pygame.draw.rect(self.screen, Color.RED.value, ( col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        if((row > 8 and row < 14 and col == 7) or (col == 6 and row == 13)):
            pygame.draw.rect(self.screen, Color.YELLOW.value, ( col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        if((col > 0 and col < 6 and row == 7) or (row == 6 and col == 1)):
            pygame.draw.rect(self.screen, Color.BLUE.value, ( col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        if((col > 8 and col < 14 and row == 7) or (row == 8 and col == 13)):
            pygame.draw.rect(self.screen, Color.GREEN.value, ( col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))