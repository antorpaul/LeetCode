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
    
    def test_WhiteSpace(self):
        s = " "
        expected: int = 1
        self.assertEqual(self.Solution.lengthOfLongestSubstring(s), expected)
    
    def test_Digits(self):
        s = " %jij%9#"
        expected: int = 5
        self.assertEqual(self.Solution.lengthOfLongestSubstring(s), expected)
    
    def test_Case342(self):
        s = "au"
        expected: int = 2
        self.assertEqual(self.Solution.lengthOfLongestSubstring(s), expected)

    def test_Case407(self):
        s = "dvdf"
        expected: int = 3
        self.assertEqual(self.Solution.lengthOfLongestSubstring(s), expected)
    
    def test_Case492(self):
        s = "bbtablud"
        expected: int = 6
        self.assertEqual(self.Solution.lengthOfLongestSubstring(s), expected)