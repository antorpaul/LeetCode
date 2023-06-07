import unittest
from Solution import Solution

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.Solution = Solution()
        return super().setUp()
    
    def test_CaseOne(self):
        prices = [7,1,5,3,6,4]
        expected: int = 5

        self.assertEqual(self.Solution.maxProfit(prices), expected)


    def test_CaseTwo(self):
        prices = [7,6,4,3,1]
        expected: int = 0

        self.assertEqual(self.Solution.maxProfit(prices), expected)

    def test_CaseThree(self):
        prices = [1,2]
        expected: int = 1

        self.assertEqual(self.Solution.maxProfit(prices), expected)
    
    def test_CaseFour(self):
        prices = [2,1,2,0,1]
        expected: int = 1

        self.assertEqual(self.Solution.maxProfit(prices), expected)