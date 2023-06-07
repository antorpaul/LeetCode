class Tree:
    """ Abstract Base Class Representing Tree Strucutre """
    
    # --- Nested Position Class
    class Position:
        """ An abstraction representing the location of a single element """
        
        def element(self):
            raise NotImplementedError("Must be implemented by subclass")
        
        def __eq__(self, other):
            """ Return true if other Position represents the same location """
            raise NotImplementedError("Must be implemented by subclass")
        
        def __ne__(self, other):
            return not (self == other)
        
    # --- Abstract methods that concrete subclass must support
    def root(self):
        """ Return Position representing the tree's root (or None if empty) """
        raise NotImplementedError("Must be implemented by subclass")
    
    def parent(self, p):
        """ Return Position represnting p's parent (or None if empty) """
        raise NotImplementedError("Must be implemented by subclass")
    
    def num_children(self, p):
        """ Return the number of children that Position p has """
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        """ Generate an iteration of Positions representing p's children """
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """ Return the total number of elements in the tree """
        raise NotImplementedError("Must be implemented by subclass")
    
    # --- Concrete methods for general trees
    def is_root(self, p):
        """ Return true if Position p represents the root of the tree """
        return self.root() == p
    
    def is_leaf(self, p):
        """ Return True if Position p does not have any children """
        return self.num_children(p) == 0
    
    def is_empty(self):
        """ Return true if tree is empty """
        return len(self) == 0