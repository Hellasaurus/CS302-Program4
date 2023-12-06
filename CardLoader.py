'''CardLoader.py'''

from gathering import *
import os

class CardLoader:
    def __init__(self, path:str) -> None:
        files = [f for f in os.listdir(os.fsencode(path))]
        self.decks:Deck = []
        myGenerator = CardGenerator()

        for i in files: 
            myFile = open(b'Decks/' + i)
            newDeck = Deck()
            for line in myFile:
                if line[0] == '\n': break
                
                delimIndex = line.find(' ')
                name  = myGenerator.getCard(line[delimIndex + 1 :-1:])
                count = int(line[0:delimIndex])
                [newDeck.addCard(name) for j in range(count)]

            myFile.close()
            self.decks.append(newDeck)
        pass

