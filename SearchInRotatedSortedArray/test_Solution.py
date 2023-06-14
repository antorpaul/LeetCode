import unittest
from Solution import Solution

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def test_CaseOne(self):
        nums: list = [4,5,6,7,0,1,2]
        target: int = 0
        
        expected: int = 4
        self.assertEqual(self.sol.search(nums, target), expected)
    
    def test_CaseTwo(self):
        nums: list = [4,5,6,7,0,1,2]
        target: int = 3

        expected: int = -1
        self.assertEqual(self.sol.search(nums, target), expected)

    def test_CaseThree(self):
        nums: list = [1]
        target: int = 0

        expected: int = -1
        self.assertEqual(self.sol.search(nums, target), expected)
    
    def test_CaseFour(self):
        nums: list = [1, 2]
        target: int = 0

        expected: int = -1
        self.assertEqual(self.sol.search(nums, target), expected)
    
    def test_CaseFive(self):
        nums: list = [1, 3]
        target: int = 2

        expected: int = -1
        self.assertEqual(self.sol.search(nums, target), expected)

    def test_CaseSix(self):
        nums: list = [1, 3]
        target: int = 3

        expected: int = 1
        self.assertEqual(self.sol.search(nums, target), expected)
    
    def test_CaseSeven(self):
        nums: list = [3, 1]
        target: int = 0

        expected: int = -1
        self.assertEqual(self.sol.search(nums, target), expected)