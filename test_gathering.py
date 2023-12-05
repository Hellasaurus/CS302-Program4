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
        assert _card.type == Card("Mountain", ['Land']).type

        _card =  _Generator.getCard("Archangel of Wrath") 
        assert _card == "Archangel of Wrath"
        assert _card == Card("Archangel of Wrath", ['Creature'])
        assert _card.type == Card("Archangel of Wrath", ['Creature']).type

        _card = _Generator.getCard("Lightning Strike") 
        assert _card == "Lightning Strike"
        assert _card == Card("Lightning Strike", ['Instant'])
        assert _card.type == Card("Lightning Strike", ['Instant']).type

        _card = _Generator.getCard("Leyline Binding") 
        assert _card == "Leyline Binding"
        assert _card == Card("Leyline Binding", ['Enchantment'])
        assert _card.type == Card("Leyline Binding", ['Enchantment']).type

        assert _Generator.getCard("BADNAME") == None
        assert _Generator.getFailures()[0] == "BADNAME"
        
        assert _Generator.getCard("BADNAME") != Card("BADNAME", [])
        assert _Generator.getFailures()[1]   == "BADNAME"
        
    
class TestCard:


    def test__eq__(self):
        pass
    def test_getName(self)->str:
        pass
    def test_isCounted(self) -> bool: 
        pass
    def test__str__(self) -> str:
        pass


# class test_Collection:

#     def test_getCards(self):
#         pass    
#     def test__iadd__(self,card:Card):
#         pass    
#     def test__isub__(self, card:Card):
#         pass
#     def test_addCard(self, card):
#         pass

#     def test_has(self, card) -> bool:
#         pass
#     def test__str__(self) -> str:
#         pass
    

# class test_Deck:
    
#     def test__lt__(self, deck) -> bool:
#         pass
            
#     def test__eq__(self, deck) -> bool:
#         pass
#     def test_isLegal(self) -> bool:
#         pass        
#     def test_addCard(self, card):
#         pass    
#     def test__str__(self) -> str:
#         pass
# # Commander Class 

# class test_Commander:

#     def test_isLegal(self) -> bool:
#         pass
#     def test_setCommander(self, card:Card):
#         pass
#     def test__str__(self) -> str:
#         pass