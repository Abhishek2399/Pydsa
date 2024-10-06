"""
Implementing linked list as datastructure in python
"""
import os
from copy import copy


os.system('cls')
DOWN_ARROW_CHAR = '\n|\n▼'
SIDE_ARROW_CHAR = '->'
LOGS_ENABLE = 0
def log(func):
    def wrapper(*args, **kwargs):
        if LOGS_ENABLE:
            print('>+<'*40)
            print(f"Started -> {func.__name__}")
        func(*args, **kwargs)
        if LOGS_ENABLE:
            print(f"Ended -> {func.__name__}")
            print('>-<'*40)
    return wrapper

# Creating a class that will represent a single node of the list
class Node:
    """
        Following class represents single node of the linked list
    """
    @log
    def __init__(self, data:any=None, next_node:object=None):
        """
        Will handle creation of a single node

        Args:
            data (any, optional): actual data we are storing in our linked list. defaults to None.
            next_node (int, optional): Address corresponding to the next node. defaults to -1.
        """
        self.data = data
        self.next_node = next_node
    
    def __str__(self):
        """
        Altered the string such as to print the node
        """
        return f"({id(self)}) >> {self.data} {SIDE_ARROW_CHAR} [{self.next_node.data if self.next_node  is not None else "null"}]"



# Creating a class to handle all the linked list operations
class LinkedList:
    """
        Following class will handle all the functions related to processing of linked list
    """
    @log
    def __init__(self, data):
        """
        Will handle generation of a initial Node, which will also be the head and tial of the LinkedList

        Args:
            data (_type_): _description_
        """
        self.head:Node = Node(data=data)
        self.tail:Node = self.head

    # Method to append a new node
    @log
    def add_node(self, data:any=None):
        """
        Following function will append a new node to the existing list

        Args:
            data (any, optional): Data which will be present in the new node. defaults to None.
        """
        new_node = Node(data)
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = new_node
        self.tail = new_node
    

    # Method to insert a new node
    @log
    def insert_node(self, position:int=-1, data:any=None):
        """
        Following function will create a new node and insert it at the passed postion

        Args:
            position (int, optional): Position at which we need to insert data. defaults to -1.
            data (any, optional): Data which will be present in the new node. defaults to None.

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
    @log
    def remove_node(self, position:int=-1):
        pass


    # Method to reverse the list
    @log
    def reverse_list(self):
        """
        Method to reverse a linked list
        """
        curr, prev = self.head, None
        temp_node = copy(curr) # used for iteration purpose only as the curr_node will keep on changing
        while temp_node:
            curr = temp_node
            temp_node = temp_node.next_node
            curr.next_node = prev
            prev = curr
        self.head = curr
    

    # Method to display the created list in CMD
    @log
    def display(self, alignment:str='h'):
        """
        Method to display the linked list
        """
        if alignment not in ['h', 'v'] : 
            print('Please choose alignment from {h}-horizontal and {v}-vertical')
            return
        node = self.head
        arrow = DOWN_ARROW_CHAR if alignment.lower() == 'v' else SIDE_ARROW_CHAR
        if node.data is None and node.next_node is None : print(f"Linked List empty")
        while node:
            print(f"{node.data}{arrow if node.next_node else ''}", end='' if alignment.lower() == 'h' else '\n')
            node = node.next_node
        if alignment.lower() == 'h':print()

    # Method to find the nth element
    @log
    def find_n_element(self):
        pass


def main():
    l_list = LinkedList(11)
    l_list.add_node(17)
    l_list.add_node(19)
    l_list.add_node(21)
    l_list.add_node(23)
    print(f"Before Insertion -> ")
    l_list.display()
    l_list.insert_node(position=3, data=25)
    print(f"After Insertion -> ")
    l_list.display(alignment='h')
    l_list.reverse_list()
    print(f"After Reverse -> ")
    l_list.display(alignment='h')


if __name__ == "__main__":
    main()
