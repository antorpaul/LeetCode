import unittest
from Solution import Solution

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.Solution = Solution()
        return super().setUp()
    
    def test_CaseOne(self):
        nums = [3,4,5,1,2]
        expected: int = 1
        self.assertEqual(self.Solution.findMin(nums), expected)
    
    def test_CaseTwo(self):
        nums = [4,5,6,7,0,1,2]
        expected: int = 0
        self.assertEqual(self.Solution.findMin(nums), expected)
    
    def test_CaseThree(self):
        nums = [11,13,15,17]
        expected: int = 11
        self.assertEqual(self.Solution.findMin(nums), expected)
    
    def test_Case45(self):
        nums = [2,1]
        expected: int = 1
        self.assertEqual(self.Solution.findMin(nums), expected)
    
    def test_Case58(self):
        nums = [3,1,2]
        expected: int = 1
        self.assertEqual(self.Solution.findMin(nums), expected)
    
    def test_Case88(self):
        nums = [5,1,2,3,4]
        expected: int = 1
        self.assertEqual(self.Solution.findMin(nums), expected)
    