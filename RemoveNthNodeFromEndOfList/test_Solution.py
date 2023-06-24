import unittest
from Solution import Solution, ListNode

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def compareLists(self, given: ListNode, expected: List):
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

    def test_CaseOne(self):
        head: ListNode = ListNode.
