from queue_linked_list import SinglyLinkedListQueue

class Tree(object):
    """ An Abstract base class representing a tree structure """

    # Abstract methods that concrete subclass must support
    def root(self):
        """ Return position representing the tree's root (or None if empty) """
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """ Return Position representing p's parent (or None if p is root) """
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """ Return the number of children that Position p has """
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """ Generate an iteration of Positions representing p's children """
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """ Return the total number of elements in the tree """
        raise NotImplementedError("must be implemented by subclass")


    # ------- Concrete methods ------
    def is_root(self, p):
        """ Return True if Position p is the root """
        return self.root() == p

    def is_leaf(self, p):
        """ Return True if Position p does not have any children """
        return self.num_children(p) == 0

    def is_empty(self):
        """ Return True if tree is empty """
        return len(self) == 0

    # Concrete recursive methods for calculating depth/height
    def depth(self, p):
        """ Return the number of levels separating Position p from the root """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height2(self, p):    # time is linear in size of subtree
        """ Return the height of the subtree rooted at Position p
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        """ Return the height of the subtree rooted at Position p
        if p is None, return the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self._height2(p)     # start height 2 recursion

    # nested Position class
    class Position(object):
        def element(self):
            """ return the element stored at this position """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """ Return True if other Position represents the same location """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """ Return True if other Position represents the same location """
            return not (self == other)


    # Breadth-First Traversal
    def breadthfirst(self):
        if not self.is_empty():
            fringe = SinglyLinkedListQueue()        # known positions not yet yielded
            fringe.enqueue(self.root())             # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()                # remove from front of queue
                yield p                             # report this position
                for c in self.children(p):
                    fringe.enqueue(c)               # add children to back of queue

if __name__ == "__main__":
    mytree = Tree()