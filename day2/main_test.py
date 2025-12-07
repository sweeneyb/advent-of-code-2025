import unittest
from parameterized import parameterized
from main import is_valid

class TestOverflows(unittest.TestCase):
     
    @parameterized.expand([
        ["is_valid", "1010", False],
        ["is_valid", "101", True],
        ["is_valid", "1012", True],



    ])
    def test_part_two(self, name, input, expected):
        result = is_valid(input)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()   