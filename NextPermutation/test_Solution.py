import unittest
from Solution import Solution

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def testCaseOne(self):
        nums = [1,2,3]
        self.sol.nextPermutation(nums)
        self.assertEqual(nums, [1,3,2])

    def testCaseTwo(self):
        nums = [3,2,1]
        self.sol.nextPermutation(nums)
        self.assertEqual(nums, [1,2,3])

    def testCaseThree(self):
        nums = [1,1,5]
        self.sol.nextPermutation(nums)
        self.assertEqual(nums, [1,5,1])

    def testCaseFour(self):
        nums = [1,3,2]
        self.sol.nextPermutation(nums)
        self.assertEqual(nums, [2,1,3])
        
    def testCaseFive(self):
        pass
