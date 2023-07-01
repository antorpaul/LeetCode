import unittest
import typing
from Solution import Solution, ListNode

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def compareLists(self, given: ListNode, expected: list):
        """ Compares a linked list to an expected list """
        currNode: ListNode = given
        i: int = 0

        # Check for empty
        if len(expected) < 1:
            self.assertEqual(currNode, None)

        # Check value of each node against expected array
        while currNode != None:
            self.assertEqual(currNode.val, expected[i])
            i += 1
            currNode = currNode.next

        # Check length
        self.assertEqual(i, len(expected))

    def comparedLinkedLists(self, given: ListNode, expected: ListNode):
        """ Compares a linked list to another linked list """
        currentGiven = given
        currentExpected = expected

        if currentGiven and currentExpected:
            while currentGiven != None:
                if currentExpected:
                    self.assertEqual(currentGiven.val, currentExpected.val)
                else:
                    raise IndexError("Given list has more values than expected.")
                currentGiven = currentGiven.next
                currentExpected = currentExpected.next

        if currentExpected:
            raise IndexError("Given list does not have all expected nodes.")

    # Linked List Tests
    def test_Append(self):
        head: ListNode = ListNode.createList([1,2,3,4,5])
        head.addNode(6)
        self.comparedLinkedLists(head, ListNode.createList([1,2,3,4,5,6]))

    # Problem Tests
    def test_CaseOne(self):
        # given
        head: ListNode = ListNode.createList([1,2,3,4,5])
        expected: list[int] = [1,2,3,5]
        
        # then
        result:ListNode = self.sol.removeNthFromEnd(head, 2)

        self.compareLists(result, expected)

    def test_CaseTwo(self):
        # given
        head: ListNode = ListNode.createList([1])
        expected: list[int] = []

        # then
        result:ListNode = self.sol.removeNthFromEnd(head, 1)

        self.compareLists(result, expected)

    def test_CaseThree(self):
        # given
        head: ListNode = ListNode.createList([1,2])
        expected: list[int] = [1]

        # then
        result:ListNode = self.sol.removeNthFromEnd(head, 1)

        self.compareLists(result, expected)
