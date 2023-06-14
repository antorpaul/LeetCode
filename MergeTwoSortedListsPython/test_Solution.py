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
        list1: ListNode = ListNode.createList([1,2,4])
        list2: ListNode = ListNode.createList([1,3,4])

        list3: ListNode = self.sol.mergeTwoLists(list1, list2)

        self.compareLists(list3, [1,1,2,3,4,4])


    def test_CaseTwo(self):
        list1: ListNode = ListNode.createList([])
        list2: ListNode = ListNode.createList([])

        list3: ListNode = self.sol.mergeTwoLists(list1, list2)

        self.compareLists(list3, [])

    def test_CaseThree(self):
        list1: ListNode = ListNode.createList([])
        list2: ListNode = ListNode.createList([0])

        list3: ListNode = self.sol.mergeTwoLists(list1, list2)

        self.compareLists(list3, [0])
