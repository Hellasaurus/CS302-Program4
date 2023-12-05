'''
Player.py
'''
from gathering import *
from Tree import *

class Player :

    def __init__(self) -> None:
        self.XP:int = 0

        self.gems:int = 0
        self.collection:Collection = Collection()

        self.decks:Tree = Tree()
        self.activeDeck:int = None
        
    def __iadd__(self, card:Card):
        self.gainCard(card)

    def gainCard(self, card:Card):
        '''Adds a card to the collection'''
        self.collection.addCard(card)
    
    def addToDeck(self, card:Card, deck:Deck) :
        '''If a card is in the player's main collection, it is added to the deck'''
        # TODO add logic to check for counts - currently does not check how many of that card are in collection
        if self.Collection.has(card):
            deck += card
            return True
        return False
    
    def __iadd__(self, deck:Deck):
        self.addDeck(deck)

    def addDeck(self, deck:Deck):
        '''adds a Deck to the collection'''
        self.decks.insert(deck)

    def retrieveDeck(self, deckName:str):
        '''return a deck by name
        if 2 decks have the same name, this returns both'''
        self.decks.retrieve(deckName)
    
    def getGems(self, count:int):
        '''Adds Gems to the player's account
        Only adds gems to the account; fails on negative count'''
        if count > 0 : self.gems += count
    
    def purchaseCard(self, cost, **goods:Card ) -> bool:
        '''attempts to purchase cards
        ### Params:
        * cost - the amount of gems to pay
        * **goods - the cards that will be added on a successful transaction
        ### Return:
        * true if the transaction is a success
        * false if the transaction fails.'''
        if self.gems < cost: return False
        
        self.gems -= cost
        for i in goods: self += i
        return True

