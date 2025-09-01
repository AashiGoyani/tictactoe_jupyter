"""
AI Agents for Tic-Tac-Toe
Contains Agent, Human, RandomPlayer, and Teacher classes.
"""

import random
from game_logic import EMPTY, PLAYER_X, PLAYER_O, DRAW, emptystate, gameover, enumstates, printboard

class Agent(object):
    """Q-Learning Agent for Tic-Tac-Toe"""
    
    def __init__(self, player, verbose=False, lossval=-1, learning=True, alpha=0.99):
        self.values = {}
        self.player = player
        self.verbose = verbose
        self.lossval = lossval
        self.learning = learning
        self.epsilon = 0.1
        self.alpha = alpha
        self.prevstate = None
        self.prevscore = 0
        self.count = 0
        enumstates(emptystate(), 0, self)  

    def episode_over(self, winner):
        """Update values at end of episode"""
        self.backup(self.winnerval(winner))
        self.prevstate = None
        self.prevscore = 0

    def action(self, state):
        """Choose action using epsilon-greedy policy"""
        r = random.random()
        if r < self.epsilon:
            move = self.random(state)
            self.log('>>>>>>> Exploratory action: ' + str(move))
        else:
            move = self.greedy(state)
            self.log('>>>>>>> Best action: ' + str(move))
        state[move[0]][move[1]] = self.player
        self.prevstate = self.statetuple(state)
        self.prevscore = self.lookup(state)
        state[move[0]][move[1]] = EMPTY
        return move

    def random(self, state):
        """Choose random available move"""
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    available.append((i,j))
        return random.choice(available)

    def greedy(self, state):
        """Choose best move according to learned values"""
        maxval = -50000
        maxmove = None
        if self.verbose:
            cells = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    state[i][j] = self.player
                    val = self.lookup(state)
                    state[i][j] = EMPTY
                    if val > maxval:
                        maxval = val
                        maxmove = (i, j)
                    if self.verbose:
                        cells.append('{0:.3f}'.format(val).center(6))
                elif self.verbose:
                    cells.append(['', 'X', 'O'][state[i][j]].center(6))
        if self.verbose:
            print("----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------".format(*cells))
        self.backup(maxval)
        return maxmove

    def backup(self, nextval):
        """Q-learning update rule"""
        if self.prevstate != None and self.learning:
            self.values[self.prevstate] += self.alpha * (nextval - self.prevscore)

    def lookup(self, state):
        """Get value for a state"""
        key = self.statetuple(state)
        if not key in self.values:
            self.add(key)
        return self.values[key]

    def add(self, state):
        """Add new state to value function"""
        winner = gameover(state)
        tup = self.statetuple(state)
        self.values[tup] = self.winnerval(winner)

    def winnerval(self, winner):
        """Convert game outcome to reward value"""
        if winner == self.player:
            return 1
        elif winner == EMPTY:
            return 0.5
        elif winner == DRAW:
            return 0
        else:
            return self.lossval

    def statetuple(self, state):
        """Convert state to tuple for hashing"""
        return (tuple(state[0]),tuple(state[1]),tuple(state[2]))

    def log(self, s):
        """Print if verbose mode enabled"""
        if self.verbose:
            print(s)

class Human(object):
    """Human player interface"""
    
    def __init__(self, player):
        self.player = player

    def action(self, state):
        """Get move from human input"""
        printboard(state)
        while True:
            try:
                action = input('Your move? i.e. x,y : ')
                row, col = int(action.split(',')[0]), int(action.split(',')[1])
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if state[row][col] == EMPTY:
                        return (row, col)
                    else:
                        print("That position is already occupied! Please choose an empty square.")
                else:
                    print("Please enter coordinates between 0-2 (e.g., 1,1)")
            except (ValueError, IndexError):
                print("Invalid input! Please enter in format: x,y (e.g., 1,1)")

    def episode_over(self, winner):
        """Handle end of episode for human"""
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))

class RandomPlayer(object):
    """Random move player"""
    
    def __init__(self, player):
        self.player = player

    def action(self, state):
        """Choose random available move"""
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    available.append((i, j))
        return random.choice(available)

    def episode_over(self, winner):
        """No learning for random player"""
        pass

class Teacher:
    """ 
    A class to implement a teacher that knows the optimal playing strategy.
    Teacher returns the best move at any time given the current state of the game.
    Uses numeric board representation (0=EMPTY, 1=PLAYER_X, 2=PLAYER_O).

    Parameters
    ----------
    level : float 
        teacher ability level. This is a value between 0-1 that indicates the
        probability of making the optimal move at any given time.
    """

    def __init__(self, level=0.9):
        """
        Ability level determines the probability that the teacher will follow
        the optimal strategy as opposed to choosing a random available move.
        """
        self.ability_level = level

    def win(self, board, key=PLAYER_X):
        """ If we have two in a row and the 3rd is available, take it. """
        # Check for diagonal wins
        a = [board[0][0], board[1][1], board[2][2]]
        b = [board[0][2], board[1][1], board[2][0]]
        if a.count(EMPTY) == 1 and a.count(key) == 2:
            ind = a.index(EMPTY)
            return ind, ind
        elif b.count(EMPTY) == 1 and b.count(key) == 2:
            ind = b.index(EMPTY)
            if ind == 0:
                return 0, 2
            elif ind == 1:
                return 1, 1
            else:
                return 2, 0
        # Now check for 2 in a row/column + empty 3rd
        for i in range(3):
            c = [board[0][i], board[1][i], board[2][i]]
            d = [board[i][0], board[i][1], board[i][2]]
            if c.count(EMPTY) == 1 and c.count(key) == 2:
                ind = c.index(EMPTY)
                return ind, i
            elif d.count(EMPTY) == 1 and d.count(key) == 2:
                ind = d.index(EMPTY)
                return i, ind
        return None

    def blockWin(self, board):
        """ Block the opponent if she has a win available. """
        return self.win(board, key=PLAYER_O)

    def fork(self, board):
        """ Create a fork opportunity such that we have 2 threats to win. """
        # Check all adjacent side middles
        if board[1][0] == PLAYER_X and board[0][1] == PLAYER_X:
            if board[0][0] == EMPTY and board[2][0] == EMPTY and board[0][2] == EMPTY:
                return 0, 0
            elif board[1][1] == EMPTY and board[2][1] == EMPTY and board[1][2] == EMPTY:
                return 1, 1
        elif board[1][0] == PLAYER_X and board[2][1] == PLAYER_X:
            if board[2][0] == EMPTY and board[0][0] == EMPTY and board[2][2] == EMPTY:
                return 2, 0
            elif board[1][1] == EMPTY and board[0][1] == EMPTY and board[1][2] == EMPTY:
                return 1, 1
        elif board[2][1] == PLAYER_X and board[1][2] == PLAYER_X:
            if board[2][2] == EMPTY and board[2][0] == EMPTY and board[0][2] == EMPTY:
                return 2, 2
            elif board[1][1] == EMPTY and board[1][0] == EMPTY and board[0][1] == EMPTY:
                return 1, 1
        elif board[1][2] == PLAYER_X and board[0][1] == PLAYER_X:
            if board[0][2] == EMPTY and board[0][0] == EMPTY and board[2][2] == EMPTY:
                return 0, 2
            elif board[1][1] == EMPTY and board[1][0] == EMPTY and board[2][1] == EMPTY:
                return 1, 1
        # Check all cross corners
        elif board[0][0] == PLAYER_X and board[2][2] == PLAYER_X:
            if board[1][0] == EMPTY and board[2][1] == EMPTY and board[2][0] == EMPTY:
                return 2, 0
            elif board[0][1] == EMPTY and board[1][2] == EMPTY and board[0][2] == EMPTY:
                return 0, 2
        elif board[2][0] == PLAYER_X and board[0][2] == PLAYER_X:
            if board[2][1] == EMPTY and board[1][2] == EMPTY and board[2][2] == EMPTY:
                return 2, 2
            elif board[1][0] == EMPTY and board[0][1] == EMPTY and board[0][0] == EMPTY:
                return 0, 0
        return None

    def blockFork(self, board):
        """ Block the opponents fork if she has one available. """
        corners = [board[0][0], board[2][0], board[0][2], board[2][2]]
        # Check all adjacent side middles
        if board[1][0] == PLAYER_O and board[0][1] == PLAYER_O:
            if board[0][0] == EMPTY and board[2][0] == EMPTY and board[0][2] == EMPTY:
                return 0, 0
            elif board[1][1] == EMPTY and board[2][1] == EMPTY and board[1][2] == EMPTY:
                return 1, 1
        elif board[1][0] == PLAYER_O and board[2][1] == PLAYER_O:
            if board[2][0] == EMPTY and board[0][0] == EMPTY and board[2][2] == EMPTY:
                return 2, 0
            elif board[1][1] == EMPTY and board[0][1] == EMPTY and board[1][2] == EMPTY:
                return 1, 1
        elif board[2][1] == PLAYER_O and board[1][2] == PLAYER_O:
            if board[2][2] == EMPTY and board[2][0] == EMPTY and board[0][2] == EMPTY:
                return 2, 2
            elif board[1][1] == EMPTY and board[1][0] == EMPTY and board[0][1] == EMPTY:
                return 1, 1
        elif board[1][2] == PLAYER_O and board[0][1] == PLAYER_O:
            if board[0][2] == EMPTY and board[0][0] == EMPTY and board[2][2] == EMPTY:
                return 0, 2
            elif board[1][1] == EMPTY and board[1][0] == EMPTY and board[2][1] == EMPTY:
                return 1, 1
        # Check all cross corners (first check for double fork opp using the corners array)
        elif corners.count(EMPTY) == 1 and corners.count(PLAYER_O) == 2:
            return 1, 2
        elif board[0][0] == PLAYER_O and board[2][2] == PLAYER_O:
            if board[1][0] == EMPTY and board[2][1] == EMPTY and board[2][0] == EMPTY:
                return 2, 0
            elif board[0][1] == EMPTY and board[1][2] == EMPTY and board[0][2] == EMPTY:
                return 0, 2
        elif board[2][0] == PLAYER_O and board[0][2] == PLAYER_O:
            if board[2][1] == EMPTY and board[1][2] == EMPTY and board[2][2] == EMPTY:
                return 2, 2
            elif board[1][0] == EMPTY and board[0][1] == EMPTY and board[0][0] == EMPTY:
                return 0, 0
        return None

    def center(self, board):
        """ Pick the center if it is available. """
        if board[1][1] == EMPTY:
            return 1, 1
        return None

    def corner(self, board):
        """ Pick a corner move. """
        # Pick opposite corner of opponent if available
        if board[0][0] == PLAYER_O and board[2][2] == EMPTY:
            return 2, 2
        elif board[2][0] == PLAYER_O and board[0][2] == EMPTY:
            return 0, 2
        elif board[0][2] == PLAYER_O and board[2][0] == EMPTY:
            return 2, 0
        elif board[2][2] == PLAYER_O and board[0][0] == EMPTY:
            return 0, 0
        # Pick any corner if no opposites are available
        elif board[0][0] == EMPTY:
            return 0, 0
        elif board[2][0] == EMPTY:
            return 2, 0
        elif board[0][2] == EMPTY:
            return 0, 2
        elif board[2][2] == EMPTY:
            return 2, 2
        return None

    def sideEmpty(self, board):
        """ Pick an empty side. """
        if board[1][0] == EMPTY:
            return 1, 0
        elif board[2][1] == EMPTY:
            return 2, 1
        elif board[1][2] == EMPTY:
            return 1, 2
        elif board[0][1] == EMPTY:
            return 0, 1
        return None

    def randomMove(self, board):
        """ Chose a random move from the available options. """
        possibles = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    possibles += [(i, j)]
        return possibles[random.randint(0, len(possibles)-1)]

    def makeMove(self, board):
        """
        Trainer goes through a hierarchy of moves, making the best move that
        is currently available each time. A touple is returned that represents
        (row, col).
        """
        # Chose randomly with some probability so that the teacher does not always win
        if random.random() > self.ability_level:
            return self.randomMove(board)
        # Follow optimal strategy
        a = self.win(board)
        if a is not None:
            return a
        a = self.blockWin(board)
        if a is not None:
            return a
        a = self.fork(board)
        if a is not None:
            return a
        a = self.blockFork(board)
        if a is not None:
            return a
        a = self.center(board)
        if a is not None:
            return a
        a = self.corner(board)
        if a is not None:
            return a
        a = self.sideEmpty(board)
        if a is not None:
            return a
        return self.randomMove(board)

    def action(self, state):
        """Interface method for game system - calls makeMove with numeric board"""
        move = self.makeMove(state)
        return move


class Human:
    """Human player class for interactive play"""
    
    def __init__(self, player):
        self.player = player
        self.verbose = False
    
    def action(self, state):
        """Get move from human input"""
        from game_logic import printboard
        
        print(f"\nPlayer {'X' if self.player == PLAYER_X else 'O'}'s turn:")
        printboard(state)
        
        while True:
            try:
                print("Enter move as row,col (0-2): ", end="")
                move_input = input().strip()
                row, col = map(int, move_input.split(','))
                
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if state[row][col] == EMPTY:
                        return (row, col)
                    else:
                        print("That position is already taken!")
                else:
                    print("Invalid coordinates! Use 0-2 for both row and col.")
            except (ValueError, IndexError):
                print("Invalid input! Enter as: row,col (example: 1,2)")
    
    def episode_over(self, winner):
        """Called after game ends - no learning for human"""
        from game_logic import DRAW
        
        if winner == self.player:
            print("You won!")
        elif winner == DRAW:
            print("It's a draw!")
        else:
            print("You lost!")

