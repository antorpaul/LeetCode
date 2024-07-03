import unittest
from Solution import Solution

class test_Solution(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = Solution()
    return super().setUp()
  
  def test_CaseOne(self):
    nums1 = [1,3]
    nums2 = [2]
    result = self.sol.findMedianSortedArrays(nums1, nums2)
    self.assertEqual(result, 2.00000)

  def test_CaseTwo(self):
    nums1 = [1,2]
    nums2 = [3,4]
    result = self.sol.findMedianSortedArrays(nums1, nums2)
    self.assertEqual(result, 2.50000)

  def test_CaseThree(self):
    nums1 = [1,2,4,6,9]
    nums2 = [3,4,5,7,8]
    result = self.sol.findMedianSortedArrays(nums1, nums2)
    self.assertEqual(result, 4.5)

  def test_CaseFour(self):
    nums1 = [1,2,3,4,5,6,7,8]
    nums2 = [1,2,3,4,5]
    result = self.sol.findMedianSortedArrays(nums1, nums2)
    self.assertEqual(result, 4)
