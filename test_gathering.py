# test_gathering.py
# Daniel Melancon
# CS 302-001
# Program 4
# Pytest testing filess

from gathering import *


import pytest
import json

# Card:

    
class TestCard:

    def test_display(self):
        assert 1==1
        pass
    def test__eq__(self):
        pass
    def test_getName(self)->str:
        pass
    def test_isCounted(self) -> bool: 
        pass
    def test__str__(self) -> str:
        pass
# CardGenerator:
class test_Generator:

    def test_getCard(self) -> object:
        pass



# FORMATS = ["Commander", "Standard", "Limited"]

# MAX_COUNT = {
#     "Standard" : 4 , 
#     "Commander": 1 ,
#     "Limited"  : None
# }

# MIN_LEGAL_SIZE = {
#     "Standard" : 60 ,
#     "Commander": 99 ,
#     "Limited"  : 40
# }

# MAX_LEGAL_SIZE = {
#     "Standard" : None ,
#     "Commander": 99 ,
#     "Limited"  : None
# }


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