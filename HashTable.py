'''
David Fuller                                                                  
                                                                            
Hash Table: Using a Binary Search Tree for collisions                         
                                                                            
 1. Node Class: Stores key and information of a node                        
 2. Binary Tree Class: A self-balancing binary search tree                  
 3. Hashtable Class: A hashtable that uses a binary tree for collisions     
                                                                            
2-3-2018
'''

small_prime = 31
ascii_length = 127                                                          

class Node(object):
    '''
    Sets up a Node object.
    '''                                                      
    
    def __init__(self, key, kwargs):
        '''
        Node's init method.

        Sets up a node object with a key, values, and links to connecting nodes.
        
        Args:
            key (str): Key for lookup.
            kwargs (dict): Values to associate with key.
        '''
        
        self.key   = key
        self.info  = kwargs
        self.left  = None
        self.right = None                                 

    def __str__(self):
        '''
        Converts node to string. Output is key, any given values,
        and whether there is a left and/or right child.
        '''
        
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

class BinaryTree(object):
    '''
    Sets up a Binary Tree object.
    '''
    
    def __init__(self):
        '''
        BinaryTree's init method.

        Sets up a binary tree object. Initializes root and nodes array.
        '''
        
        self.root = None
        self.nodes = []                                               

      
    def build(self, start, end):
        '''
        Recursively builds tree. Assumes self.nodes to be in order.

        Args:
            start (int): Starting index of array to build tree from.
            end (int): Ending index.
        '''
        
        if start > end:
            return None
        
        mid = int(start + (end - start) / 2)
        node = self.nodes[mid]

        node.left = self.build(start, mid - 1)
        node.right = self.build(mid + 1, end)

        return node
      
    def insert(self, key, kwargs):
        '''
        Inserts a node into the tree.

        Args:
            key (str): Key for lookup.
            kwargs (dict): Values to associate with key.
        '''
        
        node = Node(key, kwargs)
        if not node in self.nodes:
            self.nodes.append(node)
            self.nodes = sorted(self.nodes, key=lambda x: (x.key))
        start = 0
        end = len(self.nodes) - 1
        self.root = self.build(start, end)
        
    def search(self, node, search_key):
        '''
        Ssearches tree and returns appropriate node.

        Args:
           node (Node): Node to start search from.
           search_key (str): Key to search for.

        Returns:
           Node: If found.
           None: If not.
        '''
        
        if not node:
            return node

        nodeKey = node.key
        if search_key == nodeKey:
            return node
        if search_key > nodeKey:
            return self.search(node.right, search_key)
        if search_key < nodeKey:
            return self.search(node.left, search_key)
      
    def show(self, index, node):
        '''
        Shows tree. Lists nodes of tree.

        Args:
            index (str): Node's key.
            node (Node): Node to be shown.
        '''
        
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

class Hashtable(object):
    '''
    Sets up a Hash Table object.
    '''
        
    def __init__(self):
        '''
        HashTable's init method.

        Sets up a hash table object. Initializes table with length equal to
        the numbner of ascii characters.
        '''
        
        self.table = [None] * ascii_length
        
    def calcKey(self, string):
        '''
        Calculates hash key.

        Args:
            string (str): String to have hash value calculated on.

        Returns:
            int: Hash value.
        '''
        
        key = 0
        for char in string:
            key = (small_prime * key + ord(char)) % ascii_length
        return key
    
    def insert(self, key, kwargs):
        '''
        Inserts node into hashtable

        Args:
            key (str): Node's key value.
            kwargs (dict): Values to associate with key.
        '''
        
        index = self.calcKey(key)
        cell = self.table[index]
        
        if cell:    # Tree exists            
            node = cell.search(cell.root, key)
            if not node:                
                cell.insert(key, kwargs)
            else:                
                node.info = kwargs
        else:
            self.table[index] = BinaryTree()
            self.table[index].insert(key, kwargs)

    def search(self, key):
        '''
        Searches hashtable for node based on given information.

        Args:
            key (str): Node's key value.

        Returns:
            Node: If found.
        '''
        
        index = self.calcKey(key)
        cell = self.table[index]
        if cell:
            return cell.search(cell.root, key)
        
    def show(self):
        '''
        Shows hashtable.
        '''
        
        for i in range(len(self.table)):
            if self.table[i] != None:
                self.table[i].show(str(i), self.table[i].root)                         
                                                                                

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

##      tree = BinaryTree()
##      tree.insert("4", kwargs)
##      tree.insert("7", kwargs)
##      tree.insert("2", kwargs)
##      tree.insert("5", kwargs)
##      tree.insert("1", kwargs)
##      tree.insert("6", kwargs)
##      tree.insert("3", kwargs)
##      tree.show("0", tree.root)
