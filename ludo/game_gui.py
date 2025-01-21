
import pygame
from collections import Counter
from ludo.constants import WIDTH , HEIGHT , CELL_SIZE ,greenTokenIcon ,redTokenIcon,blueTokenIcon,yellowTokenIcon , ludoIcon, Color,Player ,font 

class GameGui:
    pygame.init()
    player = Player.blue.value
    diceValue = 4
    pathOfSelectedToken = []
    def __init__(self, board):
        self.board = board  
        self.tokens = self.board.tokens
        self.validTokens = self.board.get_valid_moves(self.player,self.diceValue)
    postionInBoard=[
        (6,1),(6,2),(6,3),(6,4),(6,5),
        (5,6),(4,6),(3,6),(2,6),(1,6),(0,6),
        (0,7),(0,8),
        (1,8),(2,8),(3,8),(4,8),(5,8),
        (6,9),(6,10),(6,11),(6,12),(6,13),(6,14),
        (7,14),(8,14),
        (8,13),(8,12),(8,11),(8,10),(8,9),
        (9,8),(10,8),(11,8),(12,8),(13,8),(14,8),
        (14,7),(14,6),
        (13,6),(12,6),(11,6),(10,6),(9,6),
        (8,5),(8,4),(8,3),(8,2),(8,1),(8,0),
        (7,0),(6,0)
        ] 
    home_run = {
        Player.blue.value: [(7,1),(7,2),(7,3),(7,4),(7,5),(7,6)],
        Player.red.value: [(1,7),(2,7),(3,7),(4,7),(5,7),(6,7)],
        Player.green.value: [(7,13),(7,12),(7,11),(7,10),(7,9),(7,8)], 
        Player.yellow.value: [(13,7),(12,7),(11,7),(10,7),(9,7),(8,7)]
    }
    home_cells = {
        Player.blue.value: [(2,2),(2,3),(3,2),(3,3)],
        Player.red.value: [(2,11),(2,12),(3,11),(3,12)],
        Player.green.value: [(11,11),(11,12),(12,11),(12,12)], 
        Player.yellow.value: [(11,2),(11,3),(12,2),(12,3)]
    }
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ludo Game")
    pygame.display.set_icon(ludoIcon)
    greenIcon = pygame.transform.scale(greenTokenIcon, (35, 35))
    yellowIcon = pygame.transform.scale(yellowTokenIcon, (35, 35))
    redIcon = pygame.transform.scale(redTokenIcon, (35, 35))
    blueIcon = pygame.transform.scale(blueTokenIcon, (35, 35))
    
    def refresh(self, board,player,diceValue):
        self.board = board  
        self.tokens = self.board.tokens
        self.diceValue = diceValue
        self.player = player
        self.validTokens = self.board.get_valid_moves(self.player,self.diceValue)
        
    def getTokenPosition(self,player,tokenValue,tokenIndex):
        row:int
        col:int
        if not isinstance(tokenValue,tuple):
            if tokenValue == -1:
                row = self.home_cells[player][tokenIndex][0]   
                col = self.home_cells[player][tokenIndex][1]
            else:   
                row = self.postionInBoard[tokenValue][0] # get row
                col = self.postionInBoard[tokenValue][1] # get col
        else:
            row = self.home_run[player][tokenValue[1]][0]
            col = self.home_run[player][tokenValue[1]][1]
        return row , col     
    # select available tokens
    # def drawPathOfSelectedToken(self,player):
    #     for i in self.pathOfSelectedToken:
    #         position = self.postionInBoard[i]
    #         row = position[0]
    #         col = position[1]
    #         pygame.draw.rect(self.screen, PlayerColor[player], (col * CELL_SIZE, row *CELL_SIZE, CELL_SIZE, CELL_SIZE),2)

    def availableTokens(self,player):
        for i in self.validTokens:
            row,col = self.getTokenPosition(player,self.tokens[player][i],i)
            x= col* CELL_SIZE
            y= row* CELL_SIZE
            if(self.tokens[player][i] == -1):
                pygame.draw.circle(self.screen, Color.BLACK.value, (x + CELL_SIZE/2.2, y + CELL_SIZE/1.4), CELL_SIZE/4,3)
            else:
                pygame.draw.rect(self.screen, Color.BLACK.value, (col * CELL_SIZE, row *CELL_SIZE, CELL_SIZE, CELL_SIZE),3)
    
    def getCommonElements(self):
        lists = [self.blueTokens,self.greenTokens]
        allValues = [value for sublist in lists for value in sublist if value != -1]
        valueCounts = Counter(allValues)
        commonValues = { value:count for value, count in valueCounts.items() if count >= 2}
        return commonValues
    
    def drawIcon(self,icon,row,col,tokenPositionInBoard):
        if self.commonElements.get(tokenPositionInBoard,None):
            original_width, original_height  = icon.get_size()
            newIcon = pygame.transform.scale(icon, (original_width // self.commonElements[tokenPositionInBoard], original_height // self.commonElements[tokenPositionInBoard]))
            self.screen.blit(newIcon, (col* CELL_SIZE + CELL_SIZE/3 , row* CELL_SIZE + CELL_SIZE*(self.printedElements[tokenPositionInBoard]/self.commonElements[tokenPositionInBoard]) ))
            self.printedElements[tokenPositionInBoard]
            self.printedElements[tokenPositionInBoard] +=1
        else:        
            self.screen.blit(icon, (col* CELL_SIZE , row* CELL_SIZE))

    def drawSavePoistions(self):
        for position in self.board.safe_positions:
            row = self.postionInBoard[position][0]
            col = self.postionInBoard[position][1]
            pygame.draw.rect(self.screen, Color.GRAY.value, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def selectValidToken(self,selectedRow,selectedCol):
        indexOftokenSelected = -1
        for i in self.validTokens:
            row,col = self.getTokenPosition(self.player,self.tokens[self.player][i],i)
            if row == selectedRow and col == selectedCol:
                indexOftokenSelected = i
                break
        if indexOftokenSelected == -1: return False
        self.board.move_token(self.player,indexOftokenSelected,self.diceValue)
        self.validTokens = []
        return True
        # self.changeTurn()

    def draw_board(self):
        self.screen.fill(Color.WHITE.value)
        
        self.drawSavePoistions()
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
        
        self.drawCircleWithBoard(CELL_SIZE * 2,Color.BLUE.value,3,3)
        self.drawCircleWithBoard(CELL_SIZE * 2,Color.RED.value,12,3)
        self.drawCircleWithBoard(CELL_SIZE * 2,Color.YELLOW.value,3,12)
        self.drawCircleWithBoard(CELL_SIZE * 2,Color.GREEN.value,12,12)
        
        # self.drawPathOfSelectedToken(self.player)

        self.availableTokens(self.player)

        self.redTokens = self.board.tokens[Player.red.value] 
        self.blueTokens = self.board.tokens[Player.blue.value] 
        self.yellowTokens = self.board.tokens[Player.yellow.value] 
        self.greenTokens = self.board.tokens[Player.green.value] 

        self.commonElements = self.getCommonElements()
        self.printedElements = { value:0 for value,count in self.commonElements.items()}
        
        for i in range(len(self.redTokens)):
            tokenPosition = self.redTokens[i]
            row,col=self.getTokenPosition(Player.red.value, tokenPosition ,i)
            self.drawIcon(self.redIcon,row,col,tokenPosition)
        for i in range(len(self.blueTokens)):
            tokenPosition = self.blueTokens[i]
            row,col=self.getTokenPosition(Player.blue.value, tokenPosition ,i)
            self.drawIcon(self.blueIcon,row,col,tokenPosition)
        for i in range(len(self.yellowTokens)):
            tokenPosition = self.yellowTokens[i]
            row,col=self.getTokenPosition(Player.yellow.value, tokenPosition ,i)
            self.drawIcon(self.yellowIcon,row,col,tokenPosition)
        for i in range(len(self.greenTokens)):
            tokenPosition = self.greenTokens[i]
            row,col=self.getTokenPosition(Player.green.value, tokenPosition ,i)
            self.drawIcon(self.greenIcon,row,col,tokenPosition)
        
        self.drawDice()
    # def drawInnerRect(self , col , row ):
    #     shiftToStart = 1
    #     widthOfBoard = CELL_SIZE
    #     widthOfCell = CELL_SIZE - 2
    #     pygame.draw.rect(self.screen, Color.BLACK.value , (CELL_SIZE * col, CELL_SIZE * row,widthOfBoard,widthOfBoard))  
    #     pygame.draw.rect(self.screen, Color.WHITE.value , (CELL_SIZE * col +shiftToStart, CELL_SIZE * row +shiftToStart,widthOfCell,widthOfCell))  
    #     pygame.draw.rect(self.screen, Color.BLACK.value , (CELL_SIZE * col + CELL_SIZE, CELL_SIZE * row,widthOfBoard,widthOfBoard))  
    #     pygame.draw.rect(self.screen, Color.WHITE.value , (CELL_SIZE * col + CELL_SIZE+shiftToStart, CELL_SIZE * row +shiftToStart,widthOfCell,widthOfCell))  
    #     pygame.draw.rect(self.screen, Color.BLACK.value , (CELL_SIZE * col + CELL_SIZE, CELL_SIZE * row + CELL_SIZE,widthOfBoard,widthOfBoard))  
    #     pygame.draw.rect(self.screen, Color.WHITE.value , (CELL_SIZE * col + CELL_SIZE +shiftToStart, CELL_SIZE * row + CELL_SIZE +shiftToStart,widthOfCell,widthOfCell))  
    #     pygame.draw.rect(self.screen, Color.BLACK.value , (CELL_SIZE * col, CELL_SIZE * row + CELL_SIZE,widthOfBoard,widthOfBoard))  
    #     pygame.draw.rect(self.screen, Color.WHITE.value , (CELL_SIZE * col +shiftToStart, CELL_SIZE * row + CELL_SIZE +shiftToStart,widthOfCell,widthOfCell))  
        
    # def drawInnerCircles(self , col , row ):
    #     shiftValue = 1

    #     self.drawCircleWithBoard(CELL_SIZE // 2, Color.WHITE.value, col, row)
    #     self.drawCircleWithBoard(CELL_SIZE // 2, Color.WHITE.value, col+shiftValue, row)
    #     self.drawCircleWithBoard(CELL_SIZE // 2, Color.WHITE.value, col+shiftValue, row+shiftValue)
    #     self.drawCircleWithBoard(CELL_SIZE // 2, Color.WHITE.value, col, row+shiftValue)
        
    def drawCircleWithBoard(self, radius, color:Color, widthCenter , hightCenter):
        bordWidth = 1 
        pygame.draw.circle(self.screen, Color.WHITE.value, (CELL_SIZE * widthCenter, CELL_SIZE * hightCenter), radius)
        pygame.draw.circle(self.screen, color, (CELL_SIZE * widthCenter, CELL_SIZE * hightCenter), radius - bordWidth , 20)
    
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
    
    def drawDice(self):
        # self.diceValue
        pygame.draw.rect(self.screen, Color.WHITE.value, (0,0, CELL_SIZE, CELL_SIZE))
        text_surface = font.render(str(self.diceValue), True, Color.BLACK.value)  # Render the text with anti-aliasing and red color
        text_rect = text_surface.get_rect(center=(CELL_SIZE // 2, CELL_SIZE // 2))  # Center the text
        self.screen.blit(text_surface, text_rect)