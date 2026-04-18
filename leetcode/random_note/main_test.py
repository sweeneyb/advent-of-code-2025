import unittest
from main import Solution


class TestRansomNote(unittest.TestCase):

    def test_input1(self):
        self.assertFalse(Solution().canConstruct(ransomNote = "a", magazine = "b"))
    
    def test_input2(self):
        self.assertFalse(Solution().canConstruct(ransomNote = "aa", magazine = "ab"))

    def test_input3(self):
        self.assertTrue(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))
