import pygame
import sys
from ludo.game_gui import GameGui
from ludo.constants import CELL_SIZE,Player
import random
from ludo.board import Board
from ludo.ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player.blue.value,Player.green.value]

    def roll_dice(self) -> int:
        return random.randint(1, 6)
    
    def get_row_col_from_mouse(self,pos):
        x, y = pos
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        return row, col
    
    def play_turn(self, player: str,dice_roll) -> bool:
        print(f"\n{player} rolled a {dice_roll}")
        valid_moves = self.board.get_valid_moves(player, dice_roll)
        if not valid_moves:
            print(f"No valid moves for {player}")
            return False
        # if player == Player.blue.value:
        #     best_move = AI.expectimax(self.board, dice_roll, 1, False, False,self.players) 
        if player == Player.green.value:
            best_move = AI.expectimax(self.board, dice_roll, 1, True, False,self.players)
        
        _,self.board= best_move
        # move = AI.simple_ai(self,valid_moves,player,dice_roll)

        # self.board.move_token(player,move,dice_roll)
        return True

    # def play_game(self) -> None:
    #         turn = 0
    #         while True:
    #             current_player = self.players[turn % 2]
    #             # dice_roll = self.roll_dice()
    #             dice_roll = 4
    #             self.play_turn(current_player , dice_roll)
    #             if dice_roll != 6:
    #                 turn +=1
    #             winner = self.board.check_winner(self.players)
    #             if winner:
    #                 print(f"\n{winner} wins the game!")
    #                 break
    
    def play_game(self):
        clock = pygame.time.Clock()
        gameInterface = GameGui(self.board)
        turn = 0
        # dice_roll = self.roll_dice()
        dice_roll = 1
        while True:
            current_player = self.players[turn % 2]
            if(current_player == Player.blue.value):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if(len(gameInterface.validTokens) == 0): 
                            turn +=1
                        else:
                            pos = pygame.mouse.get_pos()
                            row, col = self.get_row_col_from_mouse(pos)
                            if gameInterface.selectValidToken(row,col) :
                                turn +=1
            else:
                dice_roll = self.roll_dice()
                print(dice_roll)
                self.play_turn(current_player , 1)
                if dice_roll != 6:
                    # for another player
                    turn +=1
                    dice_roll = self.roll_dice()
                    current_player = self.players[turn % 2]
                    gameInterface.refresh(self.board,current_player,dice_roll)

            gameInterface.draw_board()
            pygame.display.flip()
            clock.tick(60)