'''CardLoader.py'''

from gathering import *
import os

class CardLoader:
    '''Utility class that loads any decklists in the Decks and Commander directories'''

    def __init__(self, path:str) -> None:
        files = [f for f in os.listdir(os.fsencode("Decks"))]
        self.decks:Deck = []
        myGenerator = CardGenerator()

        for i in files: 
            myFile = open(b'Decks/' + i)
            data = list(myFile)
            newDeck = Deck(str(data[0]))
            for line in data[1::]:
                if line[0] == '\n': break
                
                delimIndex = line.find(' ')
                name  = myGenerator.getCard(line[delimIndex + 1 :-1:])
                count = int(line[0:delimIndex])
                [newDeck.addCard(name) for _ in range(count)]

            myFile.close()
            self.decks.append(newDeck)
        pass

        files = [f for f in os.listdir(os.fsencode("Commander"))]

        for i in files: 
            myFile = open(b'Commander/' + i)
            data = list(myFile)
            newDeck = CommanderDeck(str(data[0]))
            for line in data[1::]:
                if line[0] == '\n': break
                
                delimIndex = line.find(' ')
                name  = myGenerator.getCard(line[delimIndex + 1 :-1:])
                count = int(line[0:delimIndex])
                [newDeck.addCard(name) for _ in range(count)]
            newDeck.setCommander(newDeck.getCards()[0])

            myFile.close()
            self.decks.append(newDeck)
        pass

        

    def getDecks(self):
        return self.decks

