import random

class TreeNode:

    def __init__(self, a_data, is_red:bool = True) -> None:
        self.data  = a_data
        self.left  = None
        self.right = None
        self.red   = is_red
    
    # Node getters
    
    def getLeft(self): 
        '''Get left Node'''
        return self.left 
    
    def getRight(self): 
        '''Get Right Node''' 
        return self.right
    
    def getSide(self, right:bool):
        '''Gets a side depending on truth value of right
        ### Param: 
        * Right : bool
        ### Return: 
        * Right node if right == True
        * Left node if not right'''
        if right: return self.right
        return self.left
    
    def getData(self)  : 
        '''Get Data''' 
        return self.data    
    
    def isRed(self) -> bool: 
        '''Gets Node color \n @output :\n \tTrue = red, \n \tFalse = Black''' 
        return self.red
    
    def isBlack(self) -> bool:
        '''Gets Node color \n @output :\n \tTrue = black, \n \tFalse = Red'''
        return not self.red
    # Node setters
    
    def setLeft(self, val):
        '''Sets the value of the left node'''
        self.left  = val 
    
    def setRight(self, val):
        '''Sets the value of the right node'''
        self.right = val
    
    def setSide(self, val, right:bool):
        '''Sets a side depending on bool param
        ### Params: 
        * val: node to insert
        * right: True to set right node'''
        if right: self.right = val
        else: self.left = val

    def setData(self, val):
        '''Sets the node's data'''
        self.data  = val 
    
    def setRed(self, val:bool = True):
        '''Sets the node's parity value'''
        self.red   = val  
    
    def setBlack(self, val:bool = True):
        '''Sets the node's parity value'''
        self.red   = not val


class Tree:

    '''
    # Red Black Tree

    a balanced search tree with the following properties:

    \t1. A node is either red or black
    \t2. The root is black⚫
    \t3. If a node is red🔴, its children are black⚫
    \t4. All paths from the root to the leaves(null nodes) have the same number of black⚫ nodes.
    '''
    
    def __init__(self) -> None:
        self.root = None

    def insert(self, in_data):
        '''
        ## Insert
        Recursively adds the node to the Tree, preserving red-black constraints
        ### Params:
        \tin_data -\tdata to add, must be comparable to other data in tree.
        '''
        #if root is empty add the new node as the root.
        if not self.root : self.root = TreeNode(in_data, False); return
        skip = False
        out = self._insert_recursive_(in_data, self.root, None ,skip)
        if out : self.root = out

    def rotateLeft(self, root) -> TreeNode:
        '''## Rotate Left
        Rotates the given node left, returning the new root'''
        return self._rotate_(root, False)

    def rotateRight(self, root)-> TreeNode:
        '''## RotateRight
        Rotates the given node right, returning the new root'''
        return self._rotate_(root, True)

    def _rotate_(self, root:TreeNode, side:bool = True) -> TreeNode:
        '''
        ## Rotate
        Helper function for rotateLeft and rotateRight
        ### Params:
        * root: root of the tree to rotate
        * side: controls the direction of rotation: True=>right
        ### Return:
        * returns the pointer to the new root'''
        child:TreeNode
        child = root.getSide(not side)
        temp = child.getSide(side)
        child.setSide(root, side)
        root.setSide(temp, not side)

        # case where root is the root of the tree
        if root == self.root: self.root = child

        return child

    def _insert_recursive_(self, in_data, curr:TreeNode, parent:TreeNode, skip:bool) -> TreeNode:
        '''
        ## Insert recursive
        helper function for insert function
        ### Params:
        * in_data - data to add to new node
        * curr - reference to current node
        * parent - parent of current node
        * skip - set to True when this node has been swapped
        ### Return:
        * None if the tree is good as-is
        * Otherwise, a reference to curr. 
        '''
        child:TreeNode  # populated by recursive call
        uncle:TreeNode  # only used in some cases
        uncleSide:bool # stores uncle direction - True => Right
        childSide:bool  # stores call direction - True => Right

        # if this is called on a leaf, return a new node
        if curr == None:
            return TreeNode(in_data)

        # Compare current node's value to insert value
        curr_data = curr.getData()
        # if our value is already in the tree, return false. 
        if curr_data == in_data: return None

        childSide = (curr_data < in_data)

        next = curr.getSide(childSide)

        child = self._insert_recursive_(in_data, next, curr, skip)

        # passes child instead, used when flipped lower in tree to pass new parent's reference to new grandparent
        if next and (next.getSide(True) == curr or next.getSide(False) == curr): return next
        '''if skip:
            skip = False
            return child''' 

        # if function call returns None, we have nothing to do.
        if child == None: return None

        # attach the new Node. 
        curr.setSide(child,childSide)
        
        # if current is red and the root, make curr black
        if parent == None and curr.isRed:
            curr.setBlack()
            return curr

        #if the current node is black and its child is red, we're done
        if child.isRed() and curr.isBlack():
            return curr

        # in other cases, we will need to make uncle comparison
        uncleSide = (parent.getData() > curr.getData()) 

        uncle = parent.getSide(uncleSide)

        if curr.isRed() and (uncle != None and uncle.isRed()):
            curr.setBlack()
            uncle.setBlack()
            parent.setRed()
            return curr
        
        if curr.isRed() and (uncle == None or uncle.isBlack()):
            # check which case we have to use
            if (uncleSide == childSide): curr = self._rotate_(curr, not childSide)


            parent.setRed()
            curr.setBlack()
            temp = self._rotate_(parent, uncleSide)
            skip = True
            return temp
        
    def fancyDisplay(self):
        '''Displays the tree in the following format: 
        (data, isRed(), level)'''
        self._fancyDisplay_(self.root,0)

    def _fancyDisplay_(self,root:TreeNode, level:int):
        if not root: return
        if root != self.root: print(", ")

        out = "( " + str(root.getData()) + ", " + str(root.isRed()) + ", " + str(level) + " )"
        print(out)
        for i in [False,True]:
            self._fancyDisplay_(root.getSide(i), level + 1)

if __name__ == "__main__":
    insertVals = []
    for i in range(50):
        insertVals.append(random.randint(-100,100))
    
    print(insertVals, "\n")

    myTree = Tree()
    for i in insertVals:
        myTree.insert(i)
        myTree.fancyDisplay()
    
    myTree.fancyDisplay()