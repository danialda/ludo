from ludo.constants import Player 
class AI:        
    def applyAlgorthim(self,board, dice_roll, depth, is_maximizing_player, is_chance_node,players ,indexOfPlayer,twoPlayers = True):
        self.playerIndex = indexOfPlayer
        self.currentPlayer = players[indexOfPlayer]
        self.numOfBoards = 0 
        if(twoPlayers):
            self.opponent = players[(indexOfPlayer+2) % 4]
            # for two players
            return  self.expectiminmax_2(board, dice_roll, depth, is_maximizing_player, is_chance_node,players,float('-inf'),float('inf')),self.numOfBoards
        else:
            # for four players
            return  self.expectiminmax_4(board, dice_roll, depth, self.playerIndex, is_chance_node,players,float('-inf'),float('inf')),self.numOfBoards
    
    def expectiminmax_2(self,board, dice_roll, depth, is_maximizing_player, is_chance_node,players,alpha,beta):
        if depth == 0 or board.check_winner() is not None:  # Terminal condition
            return board.evaluate(self.playerIndex,True), board
        
        if is_chance_node:  # Chance node: Expectation over dice rolls
            expected_value = 0
            possible_dice_rolls = range(1, 7)  # Standard dice: rolls from 1 to 6
            for roll in possible_dice_rolls:
                probability = 1 / len(possible_dice_rolls)  # Uniform probability
                for new_board in board.get_possible_boards(self.currentPlayer if is_maximizing_player else self.opponent, roll):
                    eval, _ = self.expectiminmax_2(new_board, roll, depth, is_maximizing_player, False,players,alpha,beta)
                    expected_value += probability * eval
            return expected_value, None
        
        if is_maximizing_player:  # Maximizing player's turn
            max_eval = float('-inf')
            best_move = None
            for new_board in board.get_possible_boards(self.currentPlayer, dice_roll):  
                eval, _ = self.expectiminmax_2(new_board, dice_roll, depth - 1, False, True,players,alpha,beta)
                new_board.display_board()
                print(eval)
                if eval > max_eval:
                    max_eval = eval
                    best_move = new_board
                self.numOfBoards +=1
                alpha = max(alpha, eval) 
                if beta <= alpha:  
                    break
            return max_eval, best_move

        else:  # Minimizing player's turn
            min_eval = float('inf')
            best_move = None
            for new_board in board.get_possible_boards(self.opponent, dice_roll):
                eval, _ = self.expectiminmax_2(new_board, dice_roll, depth - 1, True, True,players,alpha,beta)
                new_board.display_board()
                print(eval)
                if eval < min_eval:
                    min_eval = eval     
                    best_move = new_board
                self.numOfBoards +=1
                beta = min(beta, eval) 
                if beta <= alpha:  
                    break
            return min_eval, best_move


    def expectiminmax_4(self,board, dice_roll, depth, playerIndex, is_chance_node,players,alpha,beta):
        if depth == 0 or board.check_winner() is not None:  # Terminal condition
            return board.evaluate(self.playerIndex,False), board
        
        if is_chance_node:  # Chance node: Expectation over dice rolls
            expected_value = 0
            possible_dice_rolls = range(1, 7)  # Standard dice: rolls from 1 to 6
            for roll in possible_dice_rolls:
                probability = 1 / len(possible_dice_rolls)  # Uniform probability
                for new_board in board.get_possible_boards(players[playerIndex], roll):
                    eval, _ = self.expectiminmax_4(new_board, roll, depth, playerIndex, False,players,alpha,beta)
                    expected_value += probability * eval
            return expected_value, None
        
        if(playerIndex == self.playerIndex): # Maximizing
            max_eval = float('-inf')
            best_move = None
            for new_board in board.get_possible_boards(players[playerIndex], dice_roll):  
                eval, _ = self.expectiminmax_4(new_board, dice_roll, depth - 1, (playerIndex+1) % 4 , True,players,alpha,beta)
                new_board.display_board()
                print(eval)
                if eval > max_eval:
                    max_eval = eval
                    best_move = new_board
                self.numOfBoards +=1
                alpha = max(alpha, eval) 
                if beta <= alpha:  
                    break
            return max_eval, best_move

        else:       # Minimizing
            min_eval = float('inf')
            best_move = None
            for new_board in board.get_possible_boards(players[playerIndex], dice_roll):
                eval, _ = self.expectiminmax_4(new_board, dice_roll, depth - 1, (playerIndex+1) % 4, True,players,alpha,beta)
                new_board.display_board()
                print(eval)
                if eval < min_eval:
                    min_eval = eval     
                    best_move = new_board
                self.numOfBoards +=1
                beta = min(beta, eval) 
                if beta <= alpha:  
                    break
            return min_eval, best_move


