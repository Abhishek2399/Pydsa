"""
Implementing linked list as datastructure in python
"""

DOWN_ARROW_CHAR = '\n|\n▼'
SIDE_ARROW_CHAR = '->'
# Creating a class that will represent a single node of the list
class Node:
    """
        Following class represents single node of the linked list
    """
    def __init__(self, data:any=None, next_node:object=None):
        """
        Will handle creation of a single node

        Args:
            data (any, optional): actual data we are storing in our linked list. Defaults to None.
            next_node (int, optional): Address corresponding to the next node. Defaults to -1.
        """
        self.data = data
        self.next_node = next_node


# Creating a class to handle all the linked list operations
class LinkedList:
    """
        Following class will handle all the functions related to processing of linked list
    """
    def __init__(self, data):
        """
        Will handle generation of a initial Node, which will also be the head and tial of the LinkedList

        Args:
            data (_type_): _description_
        """
        self.head:Node = Node(data=data)
        self.tail:Node = self.head


    # Method to append a new node
    def add_node(self, data:any=None):
        pass    


    # Method to insert a new node
    def insert_node(self, position:int=-1, data:any=None):
        pass


    # Method to remove node at a position
    def remove_node(self, position:int=-1):
        pass


    # Method to reverse the list
    def reverse_list(self):
        pass

    
    # Method to display the created list in CMD
    def display(self, alignment:str='h'):
        pass


    # Method to find the nth element
    def find_n_element(self):
        pass