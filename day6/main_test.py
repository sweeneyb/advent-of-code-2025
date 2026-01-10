import unittest
from parameterized import parameterized

class TestOverflows(unittest.TestCase):
     
    @parameterized.expand([
        ["is_valid", "1010", False],
        ["is_valid", "101", True],
        ["is_valid", "1012", True],

    ])
    def test_part_one(self, name, input, expected):
        result = print(input)
        self.assertEqual(expected, result)

   

if __name__ == '__main__':
    unittest.main()   