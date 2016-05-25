from linked_binary_tree import LinkedBinaryTree
from mapbase import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    """ Sorted map implementation using a binary search tree. """

    #----------- override Position class ------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """ Return key of map's key-value pair """
            return self.element()._key

        def value(self):
