
'''
gathering.py
Daniel Melancon
CS 302 - 001

Project 4/5
main hierarchy for Magic the gathering collection tracker
'''

import json

class Card:
    '''Class that contains card information.'''

    def __init__(self, name, type):
        self.name:str = name
        self.type = type

    def display(self):
        print("Name: " + self.name)
        print("Types: " + str(self.type))
        pass

    def __eq__(self, __value: object) -> bool:
        return str(__value) == self.name

    def getName(self)->str:
        '''gets the card's name - used for making lists'''
        return self.name

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

    def __init__(self, path = "StandardAtomic.json") -> None:
        Standard_path = path

        file = open(Standard_path, 'r', encoding='utf8')

        Standard_data = json.load(file)

        self.cardList = Standard_data['data']
        
        self.cache = {}


        pass

    def getCard(self, name:str) -> object:
        '''Creates an instance of the card, storing generated cards in self.cards to avoid redundant queries
        ### Param: 
        name: the name of a magic the gathering card
        ### Return:
        A card object with the appropriate attributes'''
        if name in self.cache.keys(): return self.cache[name]
        else: 
            try:
                myCard = Card(name, self.cardList[name][0]['types'])
                self.cache[name] = myCard
            except:
                print("Could not get", name)
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
        '''Add a card to the collection'''
        if type(card) is Card:
            self.cards.insert(card)

    def has(self, card) -> bool:
        '''check if a card is in the collection'''
        return (card in self.cards)
    
    def __str__(self) -> str:
        return str(self.cards)
    

class Deck (Collection):
    '''A species of Collection that enforces deckbuilding rules'''

    def __init__(self, name:str = "New Deck", format = "Standard"):
        super().__init__()
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
            
        if max( self.cards , key=list.count) > self.maxCount:
            return False
        
    def addCard(self, card):
        '''Checks:
        ## Returns:
        True if card was added, else False'''
        # TODO: Add logic to restrict card count
        if type(card) != Card: return False

        self.cards.append(card)
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
        Deck.__init__("New Commander Deck" , "Commander")

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