import pygame
import sys
from ludo.game_gui import GameGui
from ludo.constants import CELL_SIZE,Player
import random
from ludo.board import Board
from ludo.ai import AI


class Game:
    def __init__(self):
        self.ai = AI()
        self.board = Board()
        self.players = [Player.blue.value,Player.red.value,Player.green.value,Player.yellow.value]

    def roll_dice(self) -> int:
        return random.randint(1, 6)
    
    def get_row_col_from_mouse(self,pos):
        x, y = pos
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        return row, col
    
    def play_turn(self, indexOfPlayer: str,dice_roll) -> bool:
        print(f"\n{self.players[indexOfPlayer]} rolled a {dice_roll}")
        valid_moves = self.board.get_valid_moves(self.players[indexOfPlayer], dice_roll)
        if not valid_moves:
            print(f"No valid moves for {self.players[indexOfPlayer]}")
            return False
        # if player == Player.blue.value:
        #     best_move = AI.expectimax(self.board, dice_roll, 1, False, False,self.players) 
        best_move = self.ai.applyAlgorthim(self.board, dice_roll, 2, True, False,self.players,indexOfPlayer,True if self.numOfPlayers == 2 else False)
        
        _,self.board= best_move
        # move = AI.simple_ai(self,valid_moves,player,dice_roll)

        # self.board.move_token(player,move,dice_roll)
        return True

    
    def play_game(self):
        clock = pygame.time.Clock()
        gameInterface = GameGui(self.board)
        turn = 0
        self.numOfPlayers=2
        me = self.players[turn]
        dice_roll = self.roll_dice()
        turns_num = 0
        while True:
            current_player = self.players[turn % 4]
            if(current_player == me):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if(len(gameInterface.validTokens) == 0): 
                            turn +=2 if self.numOfPlayers == 2 else 1
                            turns_num = 0
                        else:
                            pos = pygame.mouse.get_pos()
                            row, col = self.get_row_col_from_mouse(pos)
                            if gameInterface.selectValidToken(row,col) :
                                turns_num += 1
                                if (dice_roll != 6 and not (self.board.hasKilled or self.board.reachTarget)) or turns_num >= 3:
                                    turn +=2 if self.numOfPlayers == 2 else 1
                                    turns_num = 0
                                else:
                                    dice_roll = self.roll_dice()
                                    current_player = self.players[turn % 4]
                                    gameInterface.refresh(self.board,current_player,dice_roll)
                                self.board.hasKilled = False
                                self.board.reachTarget = False
                                
            else:
                # print(me," : ",self.board.tokens[me])
                # print(self.players[turn%4]," : ",self.board.tokens[self.players[turn%4]])
                dice_roll = self.roll_dice()
                self.play_turn(turn%4 , dice_roll)
                print("danial")
                turns_num +=1
                if (dice_roll != 6 and not (self.board.hasKilled or self.board.reachTarget)) or turns_num >= 3:
                    turn +=2 if self.numOfPlayers == 2 else 1
                    turns_num = 0
                    current_player = self.players[turn % 4]
                    gameInterface.refresh(self.board,current_player,dice_roll)
                else:
                    dice_roll = self.roll_dice()
                self.board.hasKilled = False
                self.board.reachTarget = False
            if self.board.check_winner() != None:
                print(self.board.check_winner())
                break    
            gameInterface.draw_board()
            pygame.display.flip()
            clock.tick(60)

    # ////////////////////////////////////////////////////////

    # def play_game_test(self) -> None:
    #     turn = 0
    #     while True:
    #         current_player = self.players[turn % 2]
    #         dice_roll = self.roll_dice()
    #         self.play_turn_test(current_player , dice_roll)
    #         if dice_roll != 6:
    #             turn +=1
    #         winner = self.board.check_winner(self.players)
    #         if winner:
    #             print(f"\n{winner} wins the game!")
    #             break
    # def play_turn_test(self, player: str,dice_roll) -> bool:
    #     print(f"\n{player} rolled a {dice_roll}")
        
    #     valid_moves = self.board.get_valid_moves(player, dice_roll)
        
    #     if not valid_moves:
    #         print(f"No valid moves for {player}")
    #         return False
    #     if player == 'Red':
    #         best_move = AI.expectimax(self.board, dice_roll, 1, False, False,self.players) 
    #     if player == 'Blue':
    #         best_move = AI.expectimax(self.board, dice_roll, 1, True, False,self.players)

    #     boards = self.board.get_possible_boards(player,dice_roll)
    #     print('---------------------\nposssible boards:')
    #     for i in range(len(boards)):
    #         print (f'* possible board {i + 1} :')
    #         boards[i].display_board()
    #     print ('------------------------')
    #     _,self.board= best_move
    #     # move = AI.simple_ai(self,valid_moves,player,dice_roll)

    #     # self.board.move_token(player,move,dice_roll)
    #     return True