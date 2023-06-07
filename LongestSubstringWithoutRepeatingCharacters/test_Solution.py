import unittest
from Solution import Solution

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.Solution = Solution()
        return super().setUp()
    
    def test_CaseOne(self):
        s = "abcabcbb"
        expected: int = 3
        self.assertEqual(self.Solution.lengthOfLongestSubstring(s), expected)
    
    def test_CaseTwo(self):
        s = "bbbbb"
        expected: int = 1
        self.assertEqual(self.Solution.lengthOfLongestSubstring(s), expected)
    
    def test_CaseThree(self):
        s = "pwwkew"
        expected: int = 3
        self.assertEqual(self.Solution.lengthOfLongestSubstring(s), expected)
    