import unittest
from Solution import Solution, ListNode

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def compareLists(self, given: ListNode, expected: list):
        currNode: ListNode = given
        i:int = 0

        if len(expected) < 1:
            self.assertEqual(currNode, None)

        while currNode != None:
            self.assertEqual(currNode.val, expected[i])
            i += 1
            currNode = currNode.next
        self.assertEqual(i, len(expected))
    
    def test_CaseOne(self):
        head: ListNode = ListNode.createList([1,2,3,4,5,6])
        self.sol.reorderList(head)
        self.compareLists(head, [1,6,2,5,3,4])


    def test_CaseTwo(self):
        head: ListNode = ListNode.createList([1,2,3,4,5])
        self.sol.reorderList(head)
        self.compareLists(head, [1,5,2,4,3])