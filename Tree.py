
class TreeNode:

    def __init__(self, a_data, is_red:bool = True) -> None:
        self.data  = [a_data]
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
        * Right : True => Right'''
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
        * right: True => Right'''
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

    # Display functions
    def displayColor(self):
        '''prints the color of the current node'''
        if self.red: return ("🔴") ;
        else: return ("⚫")

    def display(self):
        return "( " + str(self.data) + ", " + self.displayColor() + ")"

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
        out = self.__insert__(in_data, self.root, None)

        if out:
            out.setBlack()
            self.root = out

    def __rotate__(self, root:TreeNode, side:bool) -> TreeNode:
        '''
        ## Rotate
        Helper function for insertion/removal
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

        if root == self.root: self.root = child

        return child

    def __insert__(self, in_data, curr:TreeNode, parent:TreeNode) -> TreeNode:
        '''
        ## Insert recursive
        helper function for insert function
        ### Params:
        * in_data - data to add to new node
        * curr - reference to current node
        * parent - parent of current node
        ### Return:
        * None if the insert value is already in the tree.
        * Otherwise, a reference to curr. 
        '''
        child:TreeNode
        uncle:TreeNode
        uncleSide:bool  # stores uncle direction - True => Right
        childSide:bool  # stores call direction  - True => Right

        if curr == None:
            return TreeNode(in_data)

        curr_data = curr.getData()[0]

        if curr_data == in_data:
            try: 
                curr.getData().append(in_data)
            except:
                pass

            return None

        childSide = (curr_data < in_data)
        next = curr.getSide(childSide)

        child = self.__insert__(in_data, next, curr)

        if child == None: 
            return None

        if curr in [child.getSide(True), child.getSide(False)]:  
            return child
        
        curr.setSide(child, childSide)

        if parent == None: 
            return curr
        
        if curr.isRed():
            
            if child.isBlack(): 
                return curr

            uncleSide = (parent.getData()[0] > curr_data) 
            uncle = parent.getSide(uncleSide)

            if (not uncle or uncle.isBlack()):
                if (uncleSide == childSide):
                    temp = self.__rotate__(curr, not childSide)

                parent.setRed()
                curr.setBlack()
                temp = self.__rotate__(parent, uncleSide)
                return temp

            curr.setBlack()
            uncle.setBlack()
            parent.setRed()
            return curr
            
    def checkValidRBTree(self) -> bool: 
        '''
        Checks the properties of the Red-Black tree:

        \t1. A node is either red or black
        \t2. The root is black⚫
        \t3. If a node is red🔴, its children are black⚫
        \t4. All paths from the root to the leaves(null nodes) have the same number of black⚫ nodes.
        '''
        #check property 2
        if self.root.isRed(): return False

        return self.__checkValidRBTree__(self.root) != -1
        
    def __checkValidRBTree__(self, curr:TreeNode) -> int:
        '''Recursive helper function for checkValidRBTree.

        returns -1 if the test fails, otherwise returns count of black nodes to bottom.
        '''
        if curr == None: return 0

        val = 0
        if curr.isBlack(): val += 1

        left:TreeNode  = curr.getLeft()
        right:TreeNode = curr.getRight()

        # check property 3
        if curr.isRed()and (left and left.isRed() or right and right.isRed()) : return -1

        # check property 4
        leftVal  = self.__checkValidRBTree__(left)
        rightVal = self.__checkValidRBTree__(right)

        if leftVal == -1 or rightVal == -1: return -1

        if leftVal == rightVal: return val + leftVal

    def display(self, order = "inorder"): 
        '''
        # Display
        Displays the nodes in order
        ### Params:
        * root
        * order (optional) control display order with:
        \t* "inorder" - default
        \t* "preorder"
        \t* "postorder"'''
                
        self.__display__(self.root, order)
    

    def __display__(self, root:TreeNode, order = "inorder"):

        if order == "inorder"  : self.__display_inorder__(root)
        if order == "preorder" : self.__display_preorder__(root)
        if order == "postorder": self.__display_postorder__(root)

    def __display_inorder__(self, root:TreeNode):
        if root == None: return

        self.__display_inorder__(root.left)
        print(root.display())
        self.__display_inorder__(root.right)

    def __display_preorder__(self, root:TreeNode):
        if root == None: return

        print(root.display())
        self.__display_preorder__(root.left)
        self.__display_preorder__(root.right)

    def __display_postorder__(self, root:TreeNode):
        if root == None: return

        self.__display_postorder__(root.left)
        self.__display_postorder__(root.right)
        print(root.display())

    def fancyDisplay(self):
        '''Displays the tree in the following format: 
        (data, isRed(), level)'''
        self.__fancyDisplay__(self.root,0)

    def __fancyDisplay__(self,root:TreeNode, level:int):
        '''Recursive helper function for fancyDisplay'''
        if not root: return

        out = root.display() + ", level:" + str(level)

        print(out)

        for i in [False,True]:
            self.__fancyDisplay__(root.getSide(i), level + 1)

    def retrieve(self, key) -> []:
        '''Searches for the value in the tree, returning the first list where element[0] evaluates equal to key.'''
        return self.__retrieve__(self.root, key)
        
    def __retrieve__(self, curr:TreeNode, key):
        '''Recursive helper function for retrieve.'''
        if curr == None: return []
        
        curr_data = curr.getData()[0]

        if key == curr_data: return curr.getData()

        return self.__retrieve__(curr.getSide( curr_data < key ), key)
