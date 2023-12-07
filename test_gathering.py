# test_gathering.py
# Daniel Melancon
# CS 302-001
# Program 4
# Pytest testing files

from gathering import *


import pytest
import json

_Generator = CardGenerator()

class TestGenerator:

    def test_getCard(self):

        _card = _Generator.getCard("Mountain")
        assert _card  == "Mountain"
        assert _card  == Card("Mountain", ['Land'])
        assert _card._type_ == Card("Mountain", ['Land'])._type_

        _card =  _Generator.getCard("Archangel of Wrath") 
        assert _card == "Archangel of Wrath"
        assert _card == Card("Archangel of Wrath", ['Creature'])
        assert _card._type_ == Card("Archangel of Wrath", ['Creature'])._type_

        _card = _Generator.getCard("Lightning Strike") 
        assert _card == "Lightning Strike"
        assert _card == Card("Lightning Strike", ['Instant'])
        assert _card._type_ == Card("Lightning Strike", ['Instant'])._type_

        _card = _Generator.getCard("Leyline Binding") 
        assert _card == "Leyline Binding"
        assert _card == Card("Leyline Binding", ['Enchantment'])
        assert _card._type_ == Card("Leyline Binding", ['Enchantment'])._type_

        assert _Generator.getCard("BADNAME") == None
        assert _Generator.getFailures()[0] == "BADNAME"
        
        assert _Generator.getCard("BADNAME") != Card("BADNAME", [])
        assert _Generator.getFailures()[1]   == "BADNAME"
        
    
_Generator = CardGenerator()

class TestCard:

    def test_getName(self)->str:
        _names = ["Mountain", "Archangel of Wrath", "Lightning Strike", "Leyline Binding"]
        _cards = [_Generator.getCard(i) for i in _names]

        for i, card in enumerate(_cards):
            assert _names[i] == card.getName()

    def test_isCounted(self) -> bool:
        _names = ["Mountain", "Archangel of Wrath", "Lightning Strike", "Leyline Binding"]
        _passV = [False, True, True, True]
        _cards = [_Generator.getCard(i) for i in _names]

        for i, card in enumerate(_cards):
            assert _passV[i] == card.isCounted()

    def test__str__(self) -> str:
        _names = ["Mountain", "Archangel of Wrath", "Lightning Strike", "Leyline Binding"]
        _cards = [_Generator.getCard(i) for i in _names]
        _output =["Mountain ['Land']", "Archangel of Wrath ['Creature']", "Lightning Strike ['Instant']", "Leyline Binding ['Enchantment']"]

        for i, card in enumerate(_cards):
            assert _output[i] == str(card)

_Generator = CardGenerator()


class TestCollection:

    def test_getCards(self):
        pass    
    def test__iadd__isub__(self):
        cards = ['Bloodthirsty Adversary', 'Bloodthirsty Adversary', 'Bloodthirsty Adversary', 'Bloodthirsty Adversary', 'Charming Scoundrel', 'Charming Scoundrel', 'Charming Scoundrel', 'Charming Scoundrel', 'Feldon, Ronom Excavator', 'Goddric, Cloaked Reveler', 'Goddric, Cloaked Reveler', 'Goddric, Cloaked Reveler', 'Kumano Faces Kakkazan // Etching of Kumano', 'Kumano Faces Kakkazan // Etching of Kumano', 'Kumano Faces Kakkazan // Etching of Kumano', 'Kumano Faces Kakkazan // Etching of Kumano', 'Lightning Strike', 'Lightning Strike', 'Lightning Strike', 'Lightning Strike', "Mishra's Foundry", "Mishra's Foundry", "Mishra's Foundry", 'Monastery Swiftspear', 'Monastery Swiftspear', 'Monastery Swiftspear', 'Monastery Swiftspear', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', "Nahiri's Warcrafting", "Nahiri's Warcrafting", 'Play with Fire', 'Play with Fire', 'Play with Fire', 'Play with Fire', 'Shivan Devastator', 'Sokenzan, Crucible of Defiance', 'Sokenzan, Crucible of Defiance', 'Squee, Dubious Monarch', 'Squee, Dubious Monarch', 'Squee, Dubious Monarch', 'Witchstalker Frenzy', 'Witchstalker Frenzy', 'Witchstalker Frenzy']
        myCollection = Collection()

        for i in cards:
            myCollection += _Generator.getCard(i)
        
        assert str(cards) == str([card.getName() for card in myCollection.getCards()])

        for i in cards:
            myCollection -= _Generator.getCard(i)
        
        assert str([]) == str([card.getName() for card in myCollection.getCards()])


    def test_addCard(self):
        pass

    def test_has(self):
        _names = ["Mountain", "Archangel of Wrath", "Lightning Strike", "Leyline Binding"]
        _cards = [_Generator.getCard(i) for i in _names]

        _decklist = ['Bloodthirsty Adversary', 'Bloodthirsty Adversary', 'Bloodthirsty Adversary', 'Bloodthirsty Adversary', 'Charming Scoundrel', 'Charming Scoundrel', 'Charming Scoundrel', 'Charming Scoundrel', 'Feldon, Ronom Excavator', 'Goddric, Cloaked Reveler', 'Goddric, Cloaked Reveler', 'Goddric, Cloaked Reveler', 'Kumano Faces Kakkazan // Etching of Kumano', 'Kumano Faces Kakkazan // Etching of Kumano', 'Kumano Faces Kakkazan // Etching of Kumano', 'Kumano Faces Kakkazan // Etching of Kumano', 'Lightning Strike', 'Lightning Strike', 'Lightning Strike', 'Lightning Strike', "Mishra's Foundry", "Mishra's Foundry", "Mishra's Foundry", 'Monastery Swiftspear', 'Monastery Swiftspear', 'Monastery Swiftspear', 'Monastery Swiftspear', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', 'Mountain', "Nahiri's Warcrafting", "Nahiri's Warcrafting", 'Play with Fire', 'Play with Fire', 'Play with Fire', 'Play with Fire', 'Shivan Devastator', 'Sokenzan, Crucible of Defiance', 'Sokenzan, Crucible of Defiance', 'Squee, Dubious Monarch', 'Squee, Dubious Monarch', 'Squee, Dubious Monarch', 'Witchstalker Frenzy', 'Witchstalker Frenzy', 'Witchstalker Frenzy']
        myCollection = Collection()

        for i in _decklist:
            myCollection += _Generator.getCard(i)

        for i, c in enumerate(_cards):
            assert myCollection.has(c) == bool(_names[i] in _decklist)


    def test_remove(self):
        
        pass
    

class TestDeck:
            
    def test_isLegal(self):
        pass        
    def test_addCard(self):
        pass    
    def test__str__(self):
        pass
# Commander Class 

class TestCommander:

    def test_isLegal(self) -> bool:
         pass
    def test_setCommander(self, card:Card):
         pass
    def test__str__(self) -> str:
         pass