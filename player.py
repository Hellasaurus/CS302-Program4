'''
Player.py
'''
from gathering import *
import Tree

class Player :

    def __init__(self) -> None:
        self.XP = 0

        self.gems = 0
        self.collection = Collection()

        self.decks = Tree()
        self.activeDeck:int = None
        pass
        
    def gainCard(self, card:Card):
        '''Adds a card to the collection'''
        self.collection.addCard(card)
    
    def addToDeck(self, card:Card, deck:Deck) :
        '''If a card is in the player's main collection, it is added to the deck'''
        # TODO add logic to check for counts
        if Collection.has(card):
            deck.addCard(card)
            return True
        return False
    

