
'''
gathering.py
Daniel Melancon
CS 302 - 001

Project 4/5
main hierarchy for Magic the gathering collection tracker
'''
import Tree

formats = ["Commander", "Standard", "Limited"]

maxCount = {
    "Standard" : 4 , 
    "Commander": 1 ,
    "Limited"  : None
}

minLegalSize = {
    "Standard" : 60 ,
    "Commander": 99 ,
    "Limited"  : 40
}

maxLegalSize = {
    "Standard" : None ,
    "Commander": 99 ,
    "Limited"  : None
}

banList = {
    "Standard" : [],
    "Commander": [],
    "Limited"  : []
}


class Card:

    def __init__(self, name, rule):
        self.name = name

    def display():
        pass

    def getName():
        pass

class Land(Card):

    def __init__(self, name, rule, type):
        self.type = type
        super().__init__(self,name,rule)

class Spell(Card):

    def __init__(self, name, rule, cost):
        self.cost = cost
        super().__init__(self, name, rule)


class Collection:
    '''A structure that associates cards'''

    def __init__(self):
        self.cards = [] 

    def getCards(self):
        '''Fetches the list containing the collection's cards'''
        return self.cards

    def addCard(self, card):
        if type(card) is Card:
            self.cards.insert(card)

    def has(self, card) -> bool:
        return (card in self.cards)

class Deck (Collection):

    def __init__(self, format):
        super().__init__(self)
        self.format:str = format

        self.maxCount = maxCount[format]
        self.minLegalSize = minLegalSize[format]
        self.maxLegalSize = maxLegalSize[format]

    def isLegal(self) -> bool:
        '''checks if the deck follows all deckbuilding requirements'''
        if not (self.minLegalSize < len(self.cards) < self.maxLegalSize):
            return False

        duplicateCounter = {}

        for i in [ c for c in super().cards if type(c) is Spell ] :

            if not duplicateCounter[i.getName()]: 
                duplicateCounter[i.getName()] = 1
            else:
                duplicateCounter[i.getName()] += 1 
            
        if max(list(duplicateCounter)) > self.maxCount:
            return False
        
    def addCard(self, card):
        '''Checks:
        * if adding the card would exceed the format limit
        * if the card is on the banlist for the format
        ## Returns:
        True if card was added, else False'''
        if card in banList[format]:
            return False
        duplicates = len([c for c in super().cards if c == card])
        if duplicates >= maxCount:
            return False
        Collection.addCard(card)
        return True
        
class CommanderDeck(Deck):
    '''A commander deck follows the following construction rules:
    * There is a special card called the commander that follows additional rules
    * Decks must be exactly 99 cards and can have no duplicate spellse
    * Decks must be within the identity of the commander'''
    def __init__(self):
        super().__init__(self, "Commander")

        self.Commander:Card = None
        self.identity = None
    
    def isLegal(self) -> bool:
        if not super().isLegal():
            return False
        # TODO commander identity check
