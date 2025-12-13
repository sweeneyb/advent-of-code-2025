import unittest
from parameterized import parameterized
from main import get_batteries, line_joltage, find_max_of

class TestJoltage(unittest.TestCase):
     
    @parameterized.expand([
        ["987654321111111", 98],
        ["811111111111119", 89],
        ["811111111111119", 89],
        ["234234234234278", 78],
        ["818181911112111", 92],
        ["891111111111111", 91],
        ["111786111111111", 86],
        ["111111111111191", 91],
        ["111111111111111", 11],
        ["761111111111111", 76],
        ["9858686597596773748753749799295644989994688889487688987859485846957576965879798984487659967855866867", 99],
        ["2423234342822232333331233232323223351423324226323516532324213232322122223144294222372733333233333323", 97],
        ["7383383448669853327488444395431356632533467643668433447312354949444179338343352833433277429334563636",99],
        ["2333473333332333233252636333563643323335332225335332332231366233331133433333333332524346323332335494",94],

    ])
    def test_part_one(self, input, expected):
        biggest, bigger = get_batteries(input)
        self.assertEqual(expected, int(f"{biggest.value}{bigger.value}"))

    @parameterized.expand([
        ["987654321111111", 987654321111, 12],
        ["811111111111119", 811111111119, 12],
        ["234234234234278", 434234234278, 12],
        ["818181911112111", 888911112111, 12],
        
    ])
    def test_part_two(self, input, expected, to_keep):
        joltage = line_joltage(input, to_keep)
        self.assertEqual( expected, joltage)
    
    @parameterized.expand([
        ["3345", 0, 3, "4"],
        ["3345", 0, 4, "5"],
    ])
    def test_max_of(self, fixture, start, end, expected):
        index = find_max_of(fixture, start, end)
        self.assertEqual(fixture[index], expected)