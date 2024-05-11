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
