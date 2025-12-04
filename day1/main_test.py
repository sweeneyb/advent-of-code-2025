import unittest
from main import get_next_digit

class TestStringMethods(unittest.TestCase):

    def test_R1(self):
        next = get_next_digit(50, "R1")
        self.assertEqual(51, next)
    
    def test_overflow(self):
        next = get_next_digit(50, "R51")
        self.assertEqual(1, next)

    def test_underflow(self):
        next = get_next_digit(50, "L51")
        self.assertEqual(99, next)

    def test_big_underflow(self):
        next = get_next_digit(50, "L551")
        self.assertEqual(99, next)

if __name__ == '__main__':
    unittest.main()