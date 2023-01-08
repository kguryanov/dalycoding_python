import logging
import time
import unittest
from statistics import mean
from typing import Callable

from problem00004.impl.lowest_missing_int import lowest_int_sorted, lowest_int_set, lowest_int_sort_positives


class MyTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
        logging.basicConfig(level=logging.DEBUG, format=log_format)
        # logging.basicConfig(level=logging.DEBUG)

    def test_small_middle_00005(self):
        data = [3, 4, -1, 1, -3]
        expected = 2
        self.run_all(data, expected)

    def test_small_last_00004(self):
        data = [3, 2, 1, 0]
        expected = 4
        self.run_all(data, expected)

    def test_small_middle_08000(self):
        data = list(range(-4000, 4000))
        expected = 4000
        self.run_all(data, expected)

    def test_small_last_08000(self):
        data = list(range(8000, 0, -1))
        expected = 8001
        self.run_all(data, expected)

    def test_small_last_16000(self):
        data = list(range(16000, 0, -1))
        expected = 16001
        self.run_all(data, expected)

    def test_small_last_32000(self):
        data = list(range(32000, 0, -1))
        expected = 32001
        self.run_all(data, expected)

    def test_small_last_64000(self):
        data = list(range(64000, 0, -1))
        expected = 64001
        self.run_all(data, expected)

    def test_small_last_640000(self):
        data = list(range(640000, 0, -1))
        expected = 640001
        self.run_all(data, expected)

    def test_small_last_6400000(self):
        data = list(range(6400000, 0, -1))
        expected = 6400001
        self.run_all(data, expected)

    def do_run(self, nums: list[int], expected: int, runner: Callable):
        self.logger = logging.getLogger(f'Problem 00004 - {runner.__name__:30}')
        deltas = []
        for i in range(10):
            start = time.perf_counter()
            result = runner(nums)
            end = time.perf_counter()
            self.assertEqual(expected, result)  # add assertion here
            deltas.append(end - start)

        sample_size = len(nums)
        delta = mean(deltas)
        self.logger.info(f'Array Size: {sample_size:10}; ETA: {delta : .10f}')

    def run_all(self, data, expected):
        self.do_run(data, expected, lowest_int_sorted)
        self.do_run(data, expected, lowest_int_set)
        self.do_run(data, expected, lowest_int_sort_positives)


if __name__ == '__main__':
    unittest.main()
