import unittest
import MaximumSubSequenceScore

class test_MaximumSubSequenceScore(unittest.TestCase):
    def setUp(self) -> None:
        self.Solution = MaximumSubSequenceScore.Solution()

    def assertEq(self, nums1, nums2, k, expected) -> None:
        self.assertEqual(self.Solution.maxScore(nums1, nums2, k), expected)
    
    def test_one(self):
        nums1 = [1,3,3,2]
        nums2 = [2,1,3,4]
        k = 3
        expected: int = 12
        self.assertEq(nums1, nums2, k, expected)

    def test_two(self):
        nums1 = [4,2,3,1,1]
        nums2 = [7,5,10,9,6]
        k = 1
        expected: int = 30
        self.assertEq(nums1, nums2, k, expected)
