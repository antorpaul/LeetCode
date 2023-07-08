import unittest
import typing
from Solution import Solution

class test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def test_One(self):
        given: str = "ABAB"
        k: int = 2

        expected: int = self.sol.characterReplacement(given, k)
        self.assertEqual(expected, 4)

    def test_Two(self):
        given: str = "AABABBA"
        k: int = 1

        expected: int = self.sol.characterReplacement(given, k)
        self.assertEqual(expected, 4)