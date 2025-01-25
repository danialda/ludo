
from typing import List
from ludo.constants import Player
from copy import deepcopy
class Board:
    def __init__(self):
        self.players = [Player.blue.value,Player.red.value,Player.green.value,Player.yellow.value]
        # Main track positions (0-51)
        self.board = [None] * 52 
        
        # Starting positions on main track
        self.start_positions = {Player.blue.value: 0 ,Player.red.value: 13, Player.green.value: 26 ,Player.yellow.value: 39}
        
        # Home positions for each player
        self.tokens = {
            Player.red.value: [-1, -1, -1, -1],   # -1 means token is in yard
            Player.blue.value: [-1, -1, -1, -1],
            Player.yellow.value: [-1, -1, -1, -1],
            Player.green.value: [-1, -1, -1, -1],
        }
        
        # Home run tracks (6 spaces before finishing)
        self.home_runs = {
            Player.red.value: [None] * 6,
            Player.blue.value: [None] * 6,
            Player.green.value: [None] * 6,
            Player.yellow.value: [None] * 6
        }
        
        # Where tokens enter home run
        self.home_run_entries = {Player.blue.value: 50, Player.green.value: 24, Player.yellow.value: 37, Player.red.value: 11}

        self.safe_positions = [0, 8, 13, 21, 26, 34, 39, 47] 
        
        self.hasKilled = False
        self.reachTarget = False

    def is_valid_move(self, player: str, token_index: int, steps: int) -> bool:
        current_pos = self.tokens[player][token_index]
        
        # Token in yard needs a 6 to start
        if current_pos == -1:
            return steps == 6
            
        # Check if token is in home run
        if isinstance(current_pos, tuple):
            home_run_pos = current_pos[1]
            new_pos = home_run_pos + steps
            return new_pos < 6  # Must land exactly in finishing square
            
        # # Calculate new position on main track
        new_pos = current_pos + steps
        
        opponent_walls = {}
        for opponent in self.players:
            if(opponent != player):
                opponent_walls = self.getWall(opponent,opponent_walls) # get walls for every player 
        # Get positions where opponents has walls
        for wall_pos, count in opponent_walls.items():
            # print('opponent-wall' , opponent_walls)
            # If wall is between current position and new position
            # and new position is NOT beyond the wall, move is invalid
            if not (current_pos <= self.home_run_entries[player] and wall_pos > self.home_run_entries[player]): # check if wall not after home run entries    
                if current_pos < wall_pos < new_pos:
                    return False
        return True
    
    def get_valid_moves(self, player: str, dice_roll: int) -> List[int]:
        valid_moves = []
        for i in range(4):
            if self.is_valid_move(player, i, dice_roll):
                valid_moves.append(i)
        return valid_moves
    
    def get_possible_boards(self, player, dice_roll):
        boards = []
        moves = self.get_valid_moves(player,dice_roll)
        for move in moves:
            board = deepcopy(self)
            board.move_token(player,move,dice_roll)
            boards.append(board)
        return boards
    
    
    def send_token_home(self, player: str, position: int) -> None:
        # print(player)
        # print(self.tokens[player])
        self.hasKilled = True
        for i in range (4):
            if self.tokens[player][i] == position:
                self.tokens[player][i] = -1

    def move_token(self, player: str, token_index: int, steps: int) -> bool:
        current_pos = self.tokens[player][token_index]
        
        # Moving from yard to start position
        if current_pos == -1:
            if steps == 6:
                start_pos = self.start_positions[player]
                self.board[start_pos] = player
                self.tokens[player][token_index] = start_pos
                return True
            return False
            
        # Moving in home run
        if isinstance(current_pos, tuple):
            home_run_pos = current_pos[1]
            new_pos = home_run_pos + steps
            if new_pos < 6:
                self.home_runs[player][home_run_pos] = None
                self.home_runs[player][new_pos] = player
                self.tokens[player][token_index] = (player, new_pos)
                if(new_pos == 5): self.reachTarget = True
                return True
            return False
            
        
        # Calculate new position
        new_pos = (current_pos + steps) % 52
        
        # Check if token should enter home run
        entry_point = self.home_run_entries[player]
        if (current_pos <= entry_point and current_pos + steps > entry_point):
            home_run_steps = current_pos + steps - entry_point - 1 
            if home_run_steps < 6:
                self.home_runs[player][home_run_steps] = player
                self.tokens[player][token_index] = (player, home_run_steps)
                if home_run_steps == 5 : self.reachTarget = True
                return True
            return False
        # Handle capture
        if  self.board[new_pos] is not None and \
            self.board[new_pos] != player and \
            new_pos not in self.safe_positions :
            # new_pos != self.safe_positions[self.board[new_pos]]:
            self.send_token_home(self.board[new_pos], new_pos)
            
        # Clear current position if not wall
        currentPlayer = self.board[current_pos]
        self.board[current_pos] = None
        if(currentPlayer != None):
            numOfTokens = 0
            for token in self.tokens[currentPlayer]:
                if token == current_pos:
                    numOfTokens +=1
                    if(numOfTokens > 1):
                        self.board[current_pos] = currentPlayer
                        break

        # Update board and token position
        self.board[new_pos] = player
        self.tokens[player][token_index] = new_pos
        if isinstance(new_pos,tuple):
            if new_pos[1] == 5 :
                self.reachTarget = True

        return True

    def check_winner(self):
        for player in self.players:
            tokens_home = 0
            for pos in self.tokens[player]:
                if isinstance(pos, tuple) and pos[1] == 5:  # Reached end of home run
                    tokens_home += 1
            if tokens_home == 4:
                return player
        return None
    

    def getWall(self , player,walls):
        """
        1.gets the possible walls for Player               
        """
        for pos in self.tokens[player]:
            if isinstance(pos, int) and pos >= 0:  # Only consider tokens on main track
                if pos in walls.keys():
                    walls[pos] += 1
                else:
                    walls[pos] = 1
        return {key:value for key,value in walls.items() if value > 1}
    
    # def distance(self,player):
    #     distance_sum = 0
    #     player_tokens = self.tokens[player]
    #     for token in player_tokens:
    #         if isinstance(token,tuple) :
    #             distance = 5 - token[1]
    #         else:
    #             distance = self.home_run_entries[player] - token
    #         distance_sum += distance
    #     return distance_sum
    
    
    def mapTokenTo_0_50(self,token,player):
        startPos = self.start_positions[player]
        if(token >= startPos):
            return token - startPos
        else:
            return token + startPos
    
    def distance(self,player):
        distance_sum = 0
        player_tokens = self.tokens[player]
        for token in player_tokens:
            distance = 0
            
            if isinstance(token,tuple) :
                distance = 56 - (50 + token[1] + 1)
            else:
                if token == -1:
                    distance = 66  # 56+10 to    
                else:    
                    tokenPosition = self.mapTokenTo_0_50(token,player)
                    distance = 56 - tokenPosition
                
            distance_sum += distance

        return distance_sum

    # def evaluate(self):
    #     return self.distance(Player.blue.value) - self.distance(Player.green.value)


    def display_board(self) -> None:
        print("\nBoard State:")
        print("Main Track:", self.board)
        for player in self.players:
            print(f"{player} tokens:", self.tokens[player])
            print(f"{player} home run:", self.home_runs[player])

    def evaluate(self,playerIndex,towPlayers):
        if(towPlayers):
            opponent = self.players[(playerIndex+2)%4] # evaluate =   min   ----------best move 
            player = self.players[playerIndex] # evaluate =   max 
            return self.distance(opponent) - self.distance(player)
        else:
            player = self.players[playerIndex]
            distanceOfOpponents = 0
            for opponent in self.players:
                if player != opponent :
                    distanceOfOpponents += self.distance(opponent)
            return distanceOfOpponents - self.distance(player)

    
    # def display_board(self) -> None:
    #     print("\nBoard State:")
    #     print("Main Track:", self.board)
    #     for player in ['Red', 'Blue']:
    #         print(f"{player} tokens:", self.tokens[player])
    #         print(f"{player} home run:", self.home_runs[player])
    #     print(self.evaluate())
