#!/usr/bin/python3
"""Node and Singly linked list classes"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        """Initialize instance
        Args:
            data: The new node data.
            next_node: The next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve Node data"""
        return self._data

    @data.setter
    def data(self, value):
        """Property Setter.
        Args:
            value: The new data of the node.
        Raises:
            TypeError: If value is'nt int.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self._data = value

    @property
    def next_node(self):
        """Retrieve next Node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Property Setter.
        Args:
            value: The new data of the node.
        Raises:
            TypeError: If value is'nt node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList"""
    def __init__(self):
        """Initialize instance"""
        self.__head = None

    def sorted_insert(self, value):
        """Public method to insert a node.
        Args:
            value: The data of the new node.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Prints the linked list"""
        datas = []
        tmp = self.__head
        while tmp is not None:
            datas.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(datas))
