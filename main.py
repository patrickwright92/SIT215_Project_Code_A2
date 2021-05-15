from gameController import *
from random import *

# setting up the game board
class gameBoard(object):
    def __init__(self, gameBoard):
        self.gameBoard = gameBoard

    def update(self, piles, num):
        self.gameBoard[piles] -= num

    def compUpdate(self):
        self.gameBoard = computer_move(self.gameBoard, -float('inf'), float('inf'), True)[1][1]

# user validation check
def isValid(remove, gameBoard):
    #if a valid move was not parsed, or the move was not entered correctly move is not valid
    if not remove or len(remove) != 2: return False
    #if both tile and pile choice are greater than 0, and both tile and pile exist in the current game state, move is valid
    if remove[0] > 0 and remove[1] >= 0 and remove[1] < len(gameBoard) and remove[0] <= gameBoard[remove[1]]:
        return True
    #if neither of the above return false, try again.
    return False

if __name__ == "__main__":

    print("Welcome to my implementation of Game of Nim!")

    # initializing size of the game board randomly between 2 and 5 piles
    numPiles = randrange(2,5)
    tileList = []
    # distributing at least 2n + 1 tiles among n piles
    for _ in range(numPiles):
        tileList.append(randrange(numPiles+1, (numPiles*2) + 1))

    game = gameBoard(tileList)
    print("Enter the number of tiles to be removed, then space followed by the pile to remove them from (starting from 0)")
    print("The person who removes the last tile loses!")
    print("Example: to remove 5 tiles from pile 1, enter 5 1")

    player_win = True
    while True:
       #print state of the game
        print("Pile state %s" % (game.gameBoard))

        # player's turn
        player_input = str(input("Player's turn: "))
        #splitting users pile and tile inputs and adding them to the player_remove array
        player_remove = [int(i) for i in player_input.split(' ')]
        #if the player has not made a valid move, try again
        while not isValid(player_remove, game.gameBoard):
            print("Invalid move! Please input again.")
            player_input = str(input("Player turn: "))
            #splitting users pile and tile inputs and adding them to the player_remove array
            player_remove = [int(i) for i in player_input.split(' ')]
        #update game state to remove players tile from the specified pile
        game.update(player_remove[1], player_remove[0])
        #if that was the last tile, player loses
        if sum(game.gameBoard) == 0:
            player_win = False
            break
        elif sum(game.gameBoard) == 1:
            break
        #computer's turn, using gameController to choose tile to remove
        print("Computer turn")
        game.compUpdate()
        #check for game ending states, if one is reached, break and print results
        if sum(game.gameBoard) == 0:
            break
        elif sum(game.gameBoard) == 1:
            player_win = False
            break
    #in the countless times I have tested this code, the player has never won but who knows - maybe you will win?            
    if player_win:
        print(game.gameBoard)
        print("You won!")
    else:
        print(game.gameBoard)
        print("You lost!")