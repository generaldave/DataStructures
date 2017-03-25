################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# Hash Table: Using a Binary Search Tree for collisions                        #
#                                                                              #
#    1. Node Class: Stores key and information of a node                       #
#    2. Binary Tree Class: A self-balancing binary search tree                 #
#    3. Hashtable Class: A hashtable that uses a binary tree for collisions    #
#                                                                              #
# Created on 2017-3-23                                                         #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                                  CONSTANTS                                   #
#                                                                              #
################################################################################

SMALL_PRIME  = 31    # Any small prime
ASCII_LENGTH = 127   # ASCII set - 1

################################################################################
#                                                                              #
#                                 NODE CLASS                                   #
#                                                                              #
################################################################################

class Node(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, key : str, kwargs : dict) -> None:
        self.key   = key
        self.info  = kwargs
        self.left  = None
        self.right = None

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Method converts node to string. Output is key, any given values,
    # and whether there is a left and/or right child
    def __str__(self) -> None:
        message = "key: " + self.key
        for i in self.info:
            message = message + "\n" + str(i) + ": " + str(self.info[i])
        if self.left and self.right:
            message = message + "\nLeft and Right"
        elif self.left:
            message = message + "\nLeft"
        elif self.right:
            message = message + "\nRight"
        else:
            message = message + "\nNo child"
        return message

################################################################################
#                                                                              #
#                               BINARY TREE CLASS                              #
#                                                                              #
################################################################################

class BinaryTree(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
        
    def __init__(self) -> None:
        self.root = None
        self.nodes = []

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Method recursively builds tree
    # Assumes self.nodes to be in order
    def build(self, start : int, end : int) -> None:        
        if start > end:
            return None
        
        mid = int(start + (end - start) / 2)
        node = self.nodes[mid]

        node.left = self.build(start, mid - 1)
        node.right = self.build(mid + 1, end)

        return node        
        
    # Method inserts a node
    def insert(self, key : str, kwargs : dict) -> None:
        node = Node(key, kwargs)
        if not node in self.nodes:
            self.nodes.append(node)
            self.nodes = sorted(self.nodes, key=lambda x: (x.key))
        start = 0
        end = len(self.nodes) - 1
        self.root = self.build(start, end)            

    # Method searches tree and returns appropriate node
    def search(self, node : Node, searchKey: str) -> Node:        
        if not node:
            return node

        nodeKey = node.key
        if searchKey == nodeKey:
            return node
        if searchKey > nodeKey:
            return self.search(node.right, searchKey)
        if searchKey < nodeKey:
            return self.search(node.left, searchKey)

    # Method shows tree
    def show(self, index : str, node : Node) -> None:
        if node:
            if not node.left:
                print ("index: " + index)
                print (node, '\n')
            if node.left:
                self.show(index, node.left)
                print ("index: " + index)
                print (node, '\n')
            if node.right:
                self.show(index, node.right)

################################################################################
#                                                                              #
#                                HASHTABLE CLASS                               #
#                                                                              #
################################################################################

class Hashtable(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
        
    def __init__(self) -> None:
        self.table = [None] * ASCII_LENGTH

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Method calculates hash key
    def calcKey(self, string : str) -> int:
        key = 0
        for char in string:
            key = (SMALL_PRIME * key + ord(char)) % ASCII_LENGTH
        return key

    # Method insert item into hashtable
    def insert(self, key : str, kwargs : dict) -> None:        
        index = self.calcKey(key)
        cell = self.table[index]
        
        if cell:   # Tree exists            
            node = cell.search(cell.root, key)
            if not node:                
                cell.insert(key, kwargs)
            else:                
                node.info = kwargs
        else:
            self.table[index] = BinaryTree()
            self.table[index].insert(key, kwargs)

    # Method searches hashtable for node based on given information
    def search(self, key : str) -> Node:
        index = self.calcKey(key)
        cell = self.table[index]
        if cell:
            return cell.search(cell.root, key)

    # Method shows hashtable
    def show(self):
        for i in range(len(self.table)):
            if self.table[i] != None:
                self.table[i].show(str(i), self.table[i].root)

################################################################################
#                                                                              #
#                                     DEBUG                                    #
#                                                                              #
################################################################################

if __name__ == "__main__":
    table = Hashtable()

    kwargs = {'value': 0}

    string = "Hello World!"
    for char in string:        
        table.insert(char, kwargs)

    table.insert("hi", kwargs)
    table.insert("ih", kwargs)
    table.insert("hello", kwargs)
    table.insert("world", kwargs)
    table.insert("Hola", kwargs)
    table.insert("two", kwargs)

    table.show()

##    tree = BinaryTree()
##    tree.insert("4", kwargs)
##    tree.insert("7", kwargs)
##    tree.insert("2", kwargs)
##    tree.insert("5", kwargs)
##    tree.insert("1", kwargs)
##    tree.insert("6", kwargs)
##    tree.insert("3", kwargs)
##    tree.show("0", tree.root)
