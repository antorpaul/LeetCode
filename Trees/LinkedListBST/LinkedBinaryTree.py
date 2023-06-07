from Tree import Tree

class LinkedBinaryTree(Tree):
    """ Linked List Representation of Binary Tree """

    # --- Subclasses

    class Node:
        """ Singular Node in a Binary Tree """
        __slots__ = ("_element", "_parent", "_left", "_right")

        def __init__(self, element, parent=None, left=None, right=None):
            """ Lightweight non-public class for storing a node """
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:
        """ Abstraction representing the location of a single element """

        def __init__(self, container, node) -> None:
            """ Constructor not to be invoked by user """
            self._container = container
            self._node = node

        def element(self):
            """ Returns element stored at this position """
            return self._node._element
        
        def __eq__(self, other):
            """ Return True if other is a Position representing the same location. """
            return type(other) is type(self) and other._node is self._node
        
    def _validate(self, p):
        """ Return associated node if position is valid """
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type.")
        if p._container is not self:
            raise ValueError("p does not belong to this container.")
        if p._node._parent is p._node:
            # the node has gotten deleted/deprecated
            raise ValueError("p is no longer valid.")
        return p._node
    
    def _make_position(self, node):
        """ Return Position instance for given node (or None if no node) """
        return self.Position(self, node) if node is not None else None
        
    # --- Binary Tree Constructor

    def __init__(self, root_value = None):
        """ Default constructor to create empty tree """
        root: LinkedBinaryTree.Node = LinkedBinaryTree.Node(root_value, None, None, None) if root_value is not None else None
        self._root: LinkedBinaryTree.Node = root
        self._size = 0
    
    # --- Public Accessors 

    def __len__(self):
        """ Returns the total number of elements in the tree """
        return self._size
    
    def root(self):
        """ Return the root position of the tree (or None if empty) """
        return self._make_position(self._root)
    
    def parent(self, p: Position):
        """ Return the Position of p's parent """
        validatedNode: LinkedBinaryTree.Node = self._validate(p)
        return self._make_position(validatedNode._parent)
    
    def left(self, p: Position):
        """ Return the Position of p's left child (or None if no left child) """
        validatedNode: LinkedBinaryTree.Node = self._validate(p)
        return self._make_position(validatedNode._left)

    def right(self, p: Position):
        """ Return the Position of p's right child (or None if no right child) """
        validatedNode: LinkedBinaryTree.Node = self._validate(p)
        return self._make_position(validatedNode._right)
    
    def num_children(self, p: Position):
        """ Return the number of children of Position p """
        validatedNode: LinkedBinaryTree.Node = self._validate(p)
        count = 0
        if validatedNode._left is not None:
            count += 1
        if validatedNode._right is not None:
            count += 1
        return count
    
    # --- Nonpublic Update
    def _add_root(self, e: int):
        """ Place element e at the root of an empty tree and return new Position 
        Raise ValueError if tree nonempty """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self.Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p: Position, e: int):
        """ Create a new left child for Position p, storing element e 
            Return the position of a new node
            Raise ValueError if Position p is invalid or p already has a left child """
        validatedNode = self._validate(p)
        if validatedNode._left is not None: 
            raise ValueError('Left child exists')
        self._size += 1
        validatedNode._left = self.Node(e, validatedNode)
        return self._make_position(validatedNode._left)
    
    def _add_right(self, p: Position, e: int) -> int:
        """ Create a new right child for Position p, storing element e 
            Return the position of a new node
            Raise ValueError if Position p is invalid or p already has a right child """
        validatedNode = self._validate(p)
        if validatedNode._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        validatedNode._right = self.Node(e, validatedNode)
        return self._make_position(validatedNode._right)
    
    def _replace(self, p: Position, e: int) -> int:
        """ Replace the element at Position p with e, and return old element """
        validatedNode = self._validate(p)
        oldElement: int = validatedNode._element
        validatedNode._element = e
        return oldElement
    
    def _delete(self, p: Position) -> int:
        """ Delete the node at Position p, and replace it with its child if any
            Return the element that had been stored at Position p
            Raise ValueError if Position p is invalid or p has two children """
        validatedNode = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        
        # Check if left or right node exists
        child = validatedNode._left if validatedNode._left else validatedNode._right
        if child is not None:
            child._parent = validatedNode._parent
        
        if validatedNode is self._root:
            self._root = child
        else:
            parent = validatedNode._parent
            if validatedNode is parent._left:
                parent._left = child
            else:
                parent._right = child
        
        self._size -= 1
        validatedNode._parent = validatedNode
        return validatedNode._element
    
    def _attach(self, p: Position, t1, t2):
        """ Attach trees t1 and t2 as left and right subtrees of external Position """
        validatedNode = self._validate(p)
        
        if not self.is_leaf(p):
            raise ValueError('Position must be a leaf')
        
        if not type(self) is type(t1) is type(t2):
            # All types must be the same
            raise TypeError('Tree types much match')
        
        self._size += len(t1) + len(t2)

        # Attach t1 and t2 to the leaves of the tree
        if not t1.is_empty():
            t1._root._parent = validatedNode
            validatedNode._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = validatedNode
            validatedNode._right = t2._root
            t2._root = None
            t2._size = 0
