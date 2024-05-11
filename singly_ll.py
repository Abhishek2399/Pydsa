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
        """
        Following function will append a new node to the existing list

        Args:
            data (any, optional): Data which will be present in the new node. Defaults to None.
        """
        new_node = Node(data)
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = new_node
        self.tail = new_node
    

    # Method to insert a new node
    def insert_node(self, position:int=-1, data:any=None):
        """
        Following function will create a new node and insert it at the passed postion

        Args:
            position (int, optional): Position at which we need to insert data. Defaults to -1.
            data (any, optional): Data which will be present in the new node. Defaults to None.

        Raises:
            Exception: If the position is not provided an Exception will be raised
        """
        if position == -1: raise Exception("No position provided for insertion")
        new_node = Node(data=data)
        node = self.head
        node_count = 1
        while node.next_node:
            node = node.next_node
            node_count += 1
            if node_count+1 == position:
                break
        temp_node = node.next_node
        node.next_node = new_node
        new_node.next_node = temp_node


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