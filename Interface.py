# interface.py
# Daniel Melancon
# CS 302 - 001
# Project 4/5
# User interface for Project 4 

import os
from CardLoader import CardLoader
from Player import Player
from gathering import *

class Interface:
    '''User interface class. State is using self.state and self.menuitems. Setting the state to a string navigates to that page in the menu, setting the state to a function calls that funciton.'''

    def __init__(self) -> None:
        #initialize player
        self.player = Player()
        
        self.state = "Main Menu"

        self.menuItems = { 
            "Main Menu" : [("Player Menu","Player Menu"), ("View Decks", "View Decks"), ("Import Decks", "Import Decks"), ("View Collection", self._collectionView_), ("Quit", None)], 
            "Player Menu": [("Add Gems", self._addGems_), ("Add Experience", self._addXP_), ("Purchase Cards", self._purchaseCards_), ("Add a Card by Name", self._addByName_),("Back", "Main Menu"), ("Quit", None)],
            "Import Decks" : [("Import All Decks", self._importAll),("Back", "Main Menu")],
            "View Decks" : [("Back", "Main Menu")],
            }
        
        self.forSale = [
            ("Lightning Strike", 100),
            ("Memory Deluge", 200),
            ("Blossoming Tortoise", 500),
            ("The Wandering Emperor", 1000),
            ("Captivating Cave", 250)
        ]

        self.generator = CardGenerator()
        

    def run(self):
        count = 0
        while count < 1000 and self.state:
            self.clear()
            try:
                self._makeScreen()
            except KeyError:
                self.state = "Main Menu"
                print ("Invalid state, returned to main menu")
            count += 1
        self.clear()
        print("Good Bye!")


    def clear(self): 
        '''clear the screen''' 
        os.system('cls||clear')

    def _getWidth_(self): 
        '''Gets the width of the terminal''' 
        return os.get_terminal_size().columns
    
    def _getHeight(self): 
        '''Gets the height of the terminal''' 
        return os.get_terminal_size().lines
    
    def __getIntInput__(self, min, max, msg:str = "Choose an option ")->int :
        '''Prompts the user for a clamped integer input'''
        done = False
        while not done:
            try: 
                userInput = int(input(msg))
                if min <= userInput and userInput <= max: done = True
            except: pass
            if not done: print("Invalid choice, please try again") 
        return userInput
    
    def _makeScreen(self):
        '''Draws the screen'''
        self._makeHeader()

        if type(self.state) == str :
            self._menu(self.state)
        
        else: self.state()

    
    def _makeHeader(self):
        '''Creates a header'''
        info = self.player.playerInfo()
        width = self._getWidth_()
        str1 = "Active player: " + info[0] + "     " + info[1] + " XP     " + info[2] + " Gems💎"
        print(str1[:width])
        print("=" * width)

    def _menu(self, state):
        '''Draws the menu and prompts the user for input, using state and self.menuItems to control options'''
        menuItems = self.menuItems[state]
        for num, (name, _ )  in enumerate(menuItems, 1):
            print(str(num) + '.', name)

        input = self.__getIntInput__(1, len(menuItems))

        self.state = menuItems[input - 1][1]

    def _addGems_(self):
        '''adds gems to the player's account'''
        self.player.getGems(self.__getIntInput__(0,100000, "Add from 0 to 100000 gems here."))
        self.state = "Player Menu"
    
    def _addXP_(self):
        '''adds xp to the player's account'''
        self.player.getXP(self.__getIntInput__(0,1000, "Add from 0 to 1000 experience points here."))
        self.state = "Player Menu"
    
    def _addByName_(self):
        '''Adds a card to the collection by name'''
        info = '''
    Type the name of a card to add it to the collection
        **NOTE: Card names must be typed Exactly, Case Sensitive!
        Only cards legal in Standard as of 12/4/2023 will work
        Some valid card names can be found in the included decklists.
        
        type '0' to go back'''
        print(info, '-' * self._getWidth_(),sep='\n')
        userInput = input("Enter a valid card name:")
        if userInput in ["0", "b", "Back"]:
            self.state = "Main Menu"
            return
        card = self.generator.getCard(userInput)
        if card:
            self.player.gainCard(card)
            print(userInput, "added to the collection!")
        else:
            print("Invalid entry, please try again.")
        input("Press [Enter] to continue.")
 
    def _purchaseCards_(self):
        '''Presents the user with some cards available for purchase.'''
        for num, (name, price ) in enumerate(self.forSale, 1):
            optionLen = 3 + len(name)
            dots = min(40, self._getWidth_()) - optionLen - 10
            print(str(num) + ".", name, "." * dots, price, "Gems")
        
        size = 1 + len(self.forSale)
        print(str(size) + ". Back")

        userInput = self.__getIntInput__(1,size)

        if userInput == size :
            self.state = "Player Menu"
            return
        
        userInput -= 1
        if self.player.purchaseCard(self.forSale[userInput][1], self.generator.getCard(self.forSale[userInput][0])):
            print(self.forSale[userInput][0], "purchased for", self.forSale[userInput][1], "gems" )
        else: 
            print("Insufficient funds")
        
        input("Press [Enter] to continue.")

    def _collectionView_(self):
        '''Views the collection'''
        self._listAsPages_(self.player.displayCollection(), "Main Menu")

    def _listAsPages_(self, book, backState = "Main Menu"):
        '''Displays a list of strings in pages
        ## Params:
        * book - a list of strings that will be split up into pages
        * backState - The value of self.state after the user exits. '''
        if not book:
            input("Nothing to display at this time... Press [Enter] to continue.")
            self.state = backState
            return
        
        size = len(book)
        perPage = self._getHeight() - 6
        pages = []

        i = 0
        while i < size:
            page = []
            for j in range(perPage):
                try : page.append(book[i + j])
                except: break
            pages.append(page)
            i += perPage
        
        done = False
        userSelection = 1
        end = len(pages)
        while not done:
            self.clear()
            [print(i) for i in pages[userSelection-1]]
            print("Page", userSelection, "of", str(end))
            msg = "Select a page, or 0 to go back."
            userSelection = self.__getIntInput__(0 ,end, msg)
            if userSelection == 0 : 
                done = True
                self.state = backState
    
    def _importAll(self):
        '''Imports all the decks from Commander and Decks files. '''
        info = '''
    Here, you may import decks from external text files.
    * Note: Files must follow the following formatting guidelines:
        * First line contains the name of the deck
        * Lines consist of a count, followed by a space, followed by the name of the card
            * Card names are Case-sensitive and whitespace sensitive.'''
        print(info)
        print("=" * self._getWidth_())
        userSelection = self.__getIntInput__(0, 1, "Press 1 to import all decks, or 0 to go back.")
        if userSelection == 0:
            self.state = "Import Decks"
            return

        loader = CardLoader("Decks")
        decks = loader.getDecks()
        [self.player.addDeck(i) for i in decks]
        for deck in decks:
            for card in deck.getCards():
                self.player.gainCard(card)




if __name__ == '__main__':

    term = Interface()

    term.run()



