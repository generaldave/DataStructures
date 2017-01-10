########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Hash Table: Using a Binary Search Tree for collisions                #
#                                                                      #
# Created on 2017-1-9                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                              CONSTANTS                               #
#                                                                      #
########################################################################

SMALL_PRIME  = 31    # Any small prime
ASCII_LENGTH = 127   # ASCII set - 1

########################################################################
#                                                                      #
#                             NODE CLASS                               #
#                                                                      #
########################################################################

class Node(object):
    def __init__(self, key: str, value: int) -> None:
        self.key   = key
        self.value = value
        self.left  = None
        self.right = None

    def setValue(self, value: int) -> None:
        self.value = value

    def getKey(self) -> str:
        return self.key

    def getValue(self) -> int:
        return self.value

    def getNode(self) -> (str, int):
        return self.key, self.value

    def __str__(self) -> str:
        return self.key + ": " + str(self.value)

########################################################################
#                                                                      #
#                          BINARY TREE CLASS                           #
#                                                                      #
########################################################################

class BinaryTree(object):
    treeHint = 'binary tree'
    
    def __init__(self) -> None:
        self.root = None

    def getRoot(self) -> Node:
        return self.root

    def getTree(self, node: Node) -> treeHint:
        if node:
            return str(node), \
            self.getTree(node.left), \
            self.getTree(node.right)

    def insert(self, string: str, value: int) -> None:
        if self.root == None:
            self.root = Node(string, value)
        else:
            current = self.root
            while True:
                if string < current.getKey():
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(string, value)
                        break
                elif string > current.getKey():
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(string, value)
                        break

    def search(self, node: Node, key: str) -> Node:
        if not node:
            return node

        nodeKey = node.getKey()
        if nodeKey == key:
            return node

        if nodeKey < key:
            return self.search(node.right, key)

        if nodeKey > key:
            return self.search(node.left, key)

########################################################################
#                                                                      #
#                           HASH TABLE CLASS                           #
#                                                                      #
########################################################################

class HashTable(object):
    tableHint = 'hash table'
    
    def __init__(self) -> None:
        self.table = [None] * ASCII_LENGTH

    def getTable(self) -> tableHint:
        return self.table        

    def calcKey(self, string: str) -> str:
        key = 0
        for char in string:
            key = (SMALL_PRIME * key + ord(char)) % ASCII_LENGTH
        return key

    def insert(self, key: str, value: int) -> None:
        index = self.calcKey(key)
        cell  = self.table[index]
        if cell:   # Tree exists            
            node = cell.search(cell.getRoot(), key)
            if not node:
                cell.insert(key, value)
            else:
                node.setValue(value)
        else:
            self.table[index] = BinaryTree()
            self.table[index].insert(key, value)

    def search(self, string: str) -> Node:
        index = self.calcKey(string)
        cell  = self.table[index]
        if cell:
            return cell.search(cell.getRoot(), string)


########################################################################
#                                                                      #
#                         DEBUGGING / TESTING                          #
#                                                                      #
########################################################################

string    = 'Hello World!'
hashTable = HashTable()

for char in string:
    hashTable.insert(char, 0)

hashTable.insert("hi", 1)
hashTable.insert("ih", 1)
hashTable.insert("hello", 1)
hashTable.insert("world", 1)
hashTable.insert("Hola", 1)
hashTable.insert("Hola", 1)
hashTable.insert("two", 0)
hashTable.insert("two", 5)

    
for i in range(ASCII_LENGTH):
    cell = hashTable.getTable()[i]
    if cell:
        print (cell.getTree(cell.getRoot()))
    else:
        print ("no tree")

node = hashTable.search('Hola')
print ()
print (node)

node = hashTable.search('Hello')
print ()
print (node)
