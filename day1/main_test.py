import unittest
from parameterized import parameterized
from main import get_next_digit, get_next_digit_with_cliks

class TestOverflows(unittest.TestCase):

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
    
    def test_clicks_overflow(self):
        next = get_next_digit_with_cliks(59, "R200")
        self.assertEqual((59, 2), next)

    def test_clicks_overflow2(self):
        next = get_next_digit_with_cliks(50, "R250")
        self.assertEqual((0, 3), next)   

    def test_clicks_underflow(self):
        next = get_next_digit_with_cliks(59, "L200")
        self.assertEqual((59, 2), next)

    def test_clicks_underflow2(self):
        next = get_next_digit_with_cliks(50, "L250")
        self.assertEqual((0, 3), next) 

    def test_clicks_underflow3(self):
        next = get_next_digit_with_cliks(50, "L150")
        self.assertEqual((0, 2), next)         

    @parameterized.expand([
        ["overflow to 0", 50, "R50", (0,1)],
        ["overflow to 0", 50, "R150", (0,2)],
        ["overflow to 0 once", 0, "R100", (0,1)],
        ["underflow to 0 1x", 0, "L100", (0,1)],
        ["underflow to 0 2x", 0, "L200", (0,2)],
        ["underflow to 0", 50, "L150", (0,2)],
        ["underflow to 95", 0, "L5", (95,0)],

    ])
    def test_part_two(self, name, start, turn, expected):
        result = get_next_digit_with_cliks(start, turn)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()