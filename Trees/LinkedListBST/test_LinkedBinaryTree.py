import unittest
from LinkedBinaryTree import LinkedBinaryTree

class test_LinkedBinaryTree(unittest.TestCase):
    """ Test LinkedList Implementation of Binary Tree """
    emptyTree: LinkedBinaryTree = LinkedBinaryTree()
    rootOnlyTree: LinkedBinaryTree = LinkedBinaryTree(5)
    balancedTree: LinkedBinaryTree = LinkedBinaryTree()
    unbalancedTree: LinkedBinaryTree = LinkedBinaryTree()

    def test_InitializeEmptyTree(self):
        """ Initializes empty tree properly """
        # Scenario: User initializes an empty tree
        # When user initializes a tree with no input

        # Then their variable should contain an empty tree
        assert(self.emptyTree.is_empty())
    
    def test_GetRoot(self):
        """ Returns the root of a tree T """
        # Scenario: User calls to get root
        # Given an expected position
        expectedPosition: LinkedBinaryTree.Position = LinkedBinaryTree.Position(None, LinkedBinaryTree.Node(5))

        # When user calls root()
        rootPosition: LinkedBinaryTree.Position = self.rootOnlyTree.root()

        # Then the expected position should equal the root position
        assert(rootPosition.__eq__(rootPosition))

    def test_GetCorrectElementFromPosition(self):
        """ Position object will return an element stored at position p """
        # Scenario: The tree wants element from position p
        # Given a tree, position, and expected value
        expectedValue: int = 10

        myTree: LinkedBinaryTree = LinkedBinaryTree()
        myTree._add_root(expectedValue)
        rootPosition: LinkedBinaryTree.Position = myTree.root()

        # When our tree ADT requests for the element
        elementValue: int = rootPosition.element()

        # Then that value should be what we expect
        assert(elementValue == expectedValue)

    def test_getsNoneRoot(self):
        """ Returns none when asked for Root of Empty Tree """
        pass

    def checksRoot(self, p: LinkedBinaryTree.Position):
        """ Returns whether or not a position holds a root """
        pass

    def getParentOfNode(self, p: LinkedBinaryTree.Position):
        """ Returns the parent of a node on the tree that is not the root """
        pass
    
    def getParentOfRootNode(self, p: LinkedBinaryTree.Position):
        """ Returns none when provided the position of root node """
        pass

    def getNumChildren(self, p: LinkedBinaryTree.Position):
        """ Returns the number of children of node at position p """
        pass

    def getChildren(self, p: LinkedBinaryTree.Position):
        """ Generate an iteration of the children at position p """
        pass

    def checkIsLeaf(self, p: LinkedBinaryTree.Position):
        """ Returns whether or not the position is a leaf """
        pass

    def getNodeCount(self):
        """ Returns the number of positions (elements) contained in tree T """
        pass

    def checkIsEmptyForEmptyTree(self):
        """ Returns true if tree is empty """
        pass

    def checkIsEmptyForNonEmptyTree(self):
        """ Returns true if tree is empty """
        pass

    def generateIterationOfPositions(self):
        """ Generates an iteration of positions in tree T """
        pass

    def generateIterationOfElements(self):
        """ Generates an iteration of elements in tree T """
        pass
