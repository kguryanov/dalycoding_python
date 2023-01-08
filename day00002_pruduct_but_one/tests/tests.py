import unittest

from day00002_pruduct_but_one.impl.multiples_but_one import with_division, no_division


class MyTestCase(unittest.TestCase):
    def test_w_division_01(self):
        nums = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(with_division(nums), expected)  # add assertion here

    def test_w_division_02(self):
        nums = [3, 2, 1]
        expected = [2, 3, 6]
        self.assertEqual(with_division(nums), expected)  # add assertion here

    def test_no_division_01(self):
        nums = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(no_division(nums), expected)  # add assertion here

    def test_n_division_02(self):
        nums = [3, 2, 1]
        expected = [2, 3, 6]
        self.assertEqual(no_division(nums), expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
