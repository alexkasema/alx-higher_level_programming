#!/usr/bin/python3

""" Node Creation """


class Node:
    """ defines a node of a singly linked list """

    def __init__(self, data, next_node = None):
        """ Initializing a new node.
        Args:
            data (int): Data that a node has.
            next_node (Node): Points to the next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Returns the data value """
        return (self.__data)

    @property
    def next_node(self):
        """ Returns the value of the next node """
        return (self.__next_node)

    @data.setter
    def data(self, value):
        """ Sets the data of the node """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ Sets the value to the next node """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


""" Singly linked list """


class SinglyLinkedList:
    """ A class that creates the singly linked list """

    def __init__(self):
        """ Initialize a linked list """
        self.head = None

    def is_empty(self):
        """ Check if head is pointing to next node
        Return:
            True if list is empty else false
        """

        return (self.head is None)

    def sorted_insert(self, value):
        """ Insert node in ascending order
        Args:
            value (int): Value to be inserted in list
        """

        new = Node(value)

        # Insert node at the beginning of the list
        if self.is_empty() or self.head.data > value:
            new.next_node = self.head
            self.head = new
        else:
            current = self.head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """ Returns the elements in the list """
        data_list = []
        current = self.head
        while current is not None:
            data_list.append(str(current.data))
            current = current.next_node
        return "\n".join(data_list)
