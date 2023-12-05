from Player import *
from Tree import *
from gathering import *
from CardLoader import CardLoader




if __name__ ==  "__main__":

    loader = CardLoader("Decks")

    playerOne:Player = Player()

    for i in loader.decks:
        playerOne.addDeck(i)

    playerOne.decks.display()


    pass