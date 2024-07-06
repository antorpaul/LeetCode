import unittest, sys
from Solution import Solution

sys.path.append("/Users/antorpaul/Git/LeetCode")
from CopyListWithRandomPointer.Solution import ListNode

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test_CaseOne(self):
        headA = ListNode.createList([4,1,8,4,5])
        headB = ListNode.createList([5,6,1])
        currA = headA
        currA = currA.next.next
        currB = headB.next.next
        currB.next = currA

        intersect = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(intersect.val, 8)

    def test_CaseTwo(self):
        headA = ListNode.createList([1,9,1,2,4])
        headB = ListNode.createList([3])
        currA = headA
        currA = currA.next.next.next
        currB = headB
        currB.next = currA

        intersect = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(intersect.val, 2)

    def test_CaseThree(self):
        headA = ListNode.createList([2,6,4])
        headB = ListNode.createList([1,5])

        intersect = self.sol.getIntersectionNode(headA, headB)
        self.assertIsNone(intersect)

    def test_Case35(self):
        headA = ListNode.createList([2,2,4,5,4])
        headB = ListNode.createList([2,2])
        currA = headA
        currA = currA.next.next
        currB = headB.next
        currB.next = currA

        intersect = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(intersect.val, 4)
