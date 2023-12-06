# interface.py
# Daniel Melancon
# CS 302 - 001
# Project 4/5
# User interface for Project 4 

import os
import argparse
from Player import Player

class Interface:
    '''User interface class. State is using self.state and self.menuitems. Setting the state to a string navigates to that page in the menu, setting the state to a function calls that funciton.'''

    def __init__(self) -> None:
        self.headerHeight = 1
        self.footerHeight = 3
        self.borderChar = '='

        self.player = Player()

        self.state = "Main Menu"

        self.menuItems = { 
            "Main Menu" : [("Player Menu","Player Menu"), ("View Decks", "View Decks"), ("Create Deck","Create Deck"), ("Quit", None)], 
            "Player Menu": [("Add Gems", self._addGems), ("Add Experience", self._addXP), ("Back", "Main Menu"), ("Quit", None)],
            "View Decks" : [("Back", "Main Menu"), ("Quit", None)],
            "Create Deck" : [("Back", "Main Menu"), ("Quit", None)],
            }
        pass

    def run(self):
        count = 0
        while count < 1000 and self.state:
            self.clear()
            self._makeScreen()
            count += 1
        self.clear()
        print("Good Bye!")


    def clear(self): 
        '''clear the screen''' 
        os.system('cls||clear')

    def _getWidth(self): 
        '''Gets the width of the terminal''' 
        return os.get_terminal_size().columns
    
    def _getHeight(self): 
        '''Gets the height of the terminal''' 
        return os.get_terminal_size().lines
    
    def __getIntInput__(self, min, max, msg:str = "Choose an option ")->int :
        '''Prompts the user for a clamped integer input'''
        done = False
        while not done:
            try: userInput = int(input(msg))
            except: pass

            if min <= userInput and userInput <= max: done = True
            else: print("Invalid choice, please try again") 
        return userInput


    
    def _makeScreen(self):
        '''Draws the screen'''
        line = 0

        line += self.headerHeight
        self._makeHeader()

        if type(self.state) == str :
            self._menu(self.state)
        
        else: self.state()

    
    def _makeHeader(self):
        '''Creates a header'''
        info = self.player.playerInfo()
        width = self._getWidth()
        str1 = "Active player: " + info[0] + "     " + info[1] + " XP     " + info[2] + "Gems"
        print(str1[:width])
        print("=" * width)

    def _menu(self, state):
        '''Draws the menu and prompts the user for input, using state and self.menuItems to control options'''
        menuItems = self.menuItems[state]
        for num, (name, _ )  in enumerate(menuItems):
            print(str(num + 1) + '.', name)

        input = self.__getIntInput__(1, len(menuItems))

        self.state = menuItems[input - 1][1]
        pass

    def _addGems(self):
        self.player.getGems(self.__getIntInput__(0,100000, "Add from 0 to 100000 gems here."))
        self.state = "Player Menu"
    
    def _addXP(self):
        self.player.getXP(self.__getIntInput__(0,1000, "Add from 0 to 1000 experience points here."))
        self.state = "Player Menu"


if __name__ == '__main__':

    term = Interface()

    term.run()



