import unittest
from Solution import Solution

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def testCaseOne(self):
        prices = [1,2,3,0,2] 
        result = self.sol.maxProfit(prices)
        self.assertEqual(result, 3)

    def testCaseTwo(self):
        prices = [1]
        result = self.sol.maxProfit(prices)
        self.assertEqual(result, 0) 
