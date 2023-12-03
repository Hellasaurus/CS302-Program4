# Hierarchy.py
# Daniel Melancon
# CS 302-001
# Program 4
# Core hierarchy


# "Constants"
MAP_TOP = 0
MAP_BOT = 36
MAP_LEFT = 0
MAP_RIGHT = 45

V_ROOMS = 2
H_ROOMS = 3

class Tile:
    '''# Tile
    contains coordinates; (0,0) is the top left corner with positive x going right and positive y going down'''
    def __init__(self,x,y) -> None:
        self._x:int = x
        self._y:int = y
    
    def get(self):
        '''# Get
        Returns a tuple containing x and y coordinates'''
        return (self._x,self._y)

    def __eq__(self, _ref: object) -> bool:
        try:
            return (self._x, self._y) == _ref.get()
        except:
            try:
                return (self._x == _ref[0] and self._y == _ref[1])
            except:
                print("invalid comparison")
                return False


class Map:
    '''# Map
    contains map information'''
    def __init__(self) -> None:
        self.data = [[0] * (MAP_RIGHT - MAP_LEFT) for i in range(MAP_BOT - MAP_TOP)]

    def generate(self):
        '''Generates the room in self.data using the following keys:
        | Key | Ref     |
        |:---:|:-------:|
        | 0   | -Empty- |
        | 1   | Floor   |
        | 2   | Wall    |
        | 3   | Door    |
        | 4   | Path    |
        '''
        pass

    def __make_room__(self, topLeft:(int,int), botRight:(int,int)):
        '''Creates a room from the top left coordinate to the bottom right coordinate'''
        for row in range(topLeft[1],botRight[1]):
            for col in range(topLeft[0],botRight[0]):
                if row == topLeft[0] or row == botRight[0] or col == topLeft[1] or col == botRight[1]:
                    self.data[row][col] = 2
                else:
                    self.data[row][col] = 1



    

class Entity:
    '''# Entity
    base class for objects that can be displayed or interacted with'''
    def __init__(self,type:str,x,y) -> None:
        
        pass

    def display():
        pass

    pass

class Actor(Entity):
    '''# Actor
    Actors are entities that take an action each turn'''
    pass


class Enemy(Actor):
    '''# Enemy
    Enemies are entities that move towards the player and attack.'''
    pass

class Player(Actor):
    '''# Player
    The player is an actor controlled by the user.'''

