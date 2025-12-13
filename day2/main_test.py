import unittest
from parameterized import parameterized
from main import is_valid, is_valid_part_two

class TestOverflows(unittest.TestCase):
     
    @parameterized.expand([
        ["is_valid", "1010", False],
        ["is_valid", "101", True],
        ["is_valid", "1012", True],

    ])
    def test_part_one(self, name, input, expected):
        result = is_valid(input)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["is_valid", "1010", False],
        ["is_valid", "101", True],
        ["is_valid", "1012", True],
        ["is_valid", "123123", False],
        ["is_valid", "123123123", False],
        ["is_valid", "1111111", False],
        ["is_valid", "1110111", True],
        ["is_valid", "1188511885", False],
        ["is_valid", "82482482", True],
        ["is_valid", "824824824", False],
        

    ])
    def test_part_two(self, name, input, expected):
        result = is_valid_part_two(input)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()   