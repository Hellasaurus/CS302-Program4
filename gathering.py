
'''
gathering.py
Daniel Melancon
CS 302 - 001

Project 4/5
main hierarchy for Magic the gathering collection tracker
'''

import json

class Card:

    def __init__(self, name, type):
        self.name:str = name
        self.type:str = type

    def display(self):
        pass

    def getName(self):
        pass

    def isCounted(self) -> bool: 
        '''Returns true if the card can only have a limited number of copies. used for determining legality'''
        return 'land' in self.type
    
    def __str__(self) -> str:
        return self.name

class CardGenerator:
    '''# Card Generator
    uses a json file containing information on magic the gathering cards to create cards. 
    
    ### Source:
    https://mtgjson.com/'''

    def __init__(self) -> None:
        Standard_path = "StandardAtomic.json"

        Standard_data = json.load(open(Standard_path, 'r', encoding='utf8'))

        self.cardList = Standard_data['data']
        
        self.cards = {}
        pass

    def getCard(self, name:str) -> object:
        '''Creates an instance of the card, storing generated cards in self.cards to avoid redundant queries
        ### Param: 
        name: the name of a magic the gathering card
        ### Return:
        A card object with the appropriate attributes'''
        if self.cards[name]: return self.cards[name]
        else: 
            try:
                myCard = Card(name, self.cardList[name]['types'])
                self.cards[name] = myCard
            except:
                print("Could not get card")
                return None
        return myCard



FORMATS = ["Commander", "Standard", "Limited"]

MAX_COUNT = {
    "Standard" : 4 , 
    "Commander": 1 ,
    "Limited"  : None
}

MIN_LEGAL_SIZE = {
    "Standard" : 60 ,
    "Commander": 99 ,
    "Limited"  : 40
}

MAX_LEGAL_SIZE = {
    "Standard" : None ,
    "Commander": 99 ,
    "Limited"  : None
}

BAN_LIST = {
    "Standard" : [],
    "Commander": [],
    "Limited"  : []
}


class Collection:
    '''A structure that associates cards'''

    def __init__(self):
        self.cards = [] 

    def getCards(self):
        '''Fetches the list containing the collection's cards'''
        return self.cards
    
    def __iadd__(self,card:Card):
        self.addCard(card)
    
    def __isub__(self, card:Card):
        self.cards.remove(card) 

    def addCard(self, card):
        if type(card) is Card:
            self.cards.insert(card)

    def has(self, card) -> bool:
        return (card in self.cards)
    
    def __str__(self) -> str:
        return str(self.cards)
    

class Deck (Collection):
    '''A species of Collection that enforces deckbuilding rules'''

    def __init__(self,name:str, format):
        super().__init__(self)
        self.name:str = name
        self.format:str = format

        self.maxCount = MAX_COUNT[format]
        self.minLegalSize = MIN_LEGAL_SIZE[format]
        self.maxLegalSize = MAX_LEGAL_SIZE[format]
    
    def __lt__(self, deck) -> bool: 
        return self.name < deck.name
    def __eq__(self, deck) -> bool:
        return self.name == deck.name

    def isLegal(self) -> bool:
        '''checks if the deck follows all deckbuilding requirements'''
        if not (self.minLegalSize < len(self.cards) < self.maxLegalSize):
            return False

        duplicateCounter = {}

        for i in [ c for c in super().cards if c.isCounted() ] :

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
        if card in BAN_LIST[format]:
            return False
        duplicates = len([c for c in super().cards if c.isCounted()])
        if duplicates >= MAX_COUNT:
            return False
        Collection.addCard(card)
        return True
    
    def __str__(self) -> str:
        '''returns the list of cards preceded by the name of the deck'''
        return self.name + ':' + super().__str__()
        
class CommanderDeck(Deck):
    '''A commander deck follows the following construction rules:
    * There is a special card called the commander that follows additional rules
    * Decks must be exactly 99 cards and can have no duplicate spellse
    * Decks must be within the identity of the commander'''
    def __init__(self, _commander:Card = None):
        super().__init__(self, "Commander")

        self.Commander:Card = _commander
        self.identity = None
    
    def isLegal(self) -> bool:
        if not super().isLegal():
            return False
        # TODO commander identity check

    def setCommander(self, card:Card):
        if self.has(card): 
            pass
        self.Commander = card

    def __str__(self) -> str:
        return self.name + '\nCommander: ' + str(self.Commander) + '\n' + Collection.__str__()