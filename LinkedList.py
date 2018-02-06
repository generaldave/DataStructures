################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# Linked List: Single link                                                     #
#                                                                              #
#    1. Node Class: Stores key and information of a node                       #
#    2. Linked List Class: A linked list                                       #
#                                                                              #
# Created on 2017-3-26                                                         #
#                                                                              #
################################################################################

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
    
    def __init__(self, key : (int, str), data : dict) -> None:
        self.key = key
        self.data = data
        self.next = None

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Method returns there is a next node or not
    def connectingNodes(self) -> str:
        if self.next:
            return "next"
        else:
            return "no next"

    # Method converts node to string. Output is key, any given values,
    # and whether there is a next node or not
    def __str__(self) -> str:
        message = "key: " + str(self.key)
        for key in self.data:
            message += "\n" + str(key) + ": " + str(self.data[key])
        message += "\n" + self.connectingNodes()
        return message

################################################################################
#                                                                              #
#                               LINKED LIST CLASS                              #
#                                                                              #
################################################################################

class LinkedList(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.count = 0

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Medthod inserts node into linked list
    def insert(self, key : (int, str), data : dict) -> None:
        node = Node(key, data)
        if not self.start:
            self.start = node

        if self.end:
            self.end.next = node

        self.end = node
        self.count += 1

    # Method searches linked list for a node and returns it if found.
    # Otherwise ruturns None
    def search(self, key : (int, str)) -> Node:
        node = self.start
        while node:
            if node.key == key:
                return node
            node = node.next
        return None

    # Method removes node from linked list. Returns node if found.
    # Otherwise returns None
    def remove(self,  key : (int, str)) -> Node:
        previous = None
        node = self.start

        while node:
            if key == node.key:
                if previous == None:
                    self.start = self.start.next
                else:
                    previous.next = node.next
                return node
            previous = node
            node = node.next
        return None

    # Method displays the linked list
    def show(self) -> None:
        node = self.start
        while node:
            print(node)
            print()
            node = node.next
            
################################################################################
#                                                                              #
#                                     DEBUG                                    #
#                                                                              #
################################################################################

if __name__ == "__main__":            
    ##node = Node(1, {'value' : 3, 'colour': 'blue'})
    ##node2 = Node(2, {'value' : 5, 'colour': 'blue'})
    ##node.next = node2
    ##node2.previous = node
    ##print(node)
    ##print()
    ##print(node2)

    thelist = LinkedList()
    thelist.insert(1, {'value' : 3, 'colour': 'blue'})
    thelist.insert(2, {'value' : 5, 'colour': 'blue'})
    thelist.insert(3, {})
    thelist.show()

    node = thelist.search(2)
    if node:
        print("FOUND")
        print(node)
    else:
        print("\nnot found")

    node = thelist.remove(3)
    if node:
        print()
        print("REMOVED")
        print(node)

    print()
    thelist.show()
    node = thelist.search(1)
    if node:
        print("FOUND")
        print(node)
    else:
        print("\nnot found")
