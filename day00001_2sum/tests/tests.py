import logging
import time
import unittest
from statistics import mean

from day00001_2sum.impl.twosum import check_if_sum_exists


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
        logging.basicConfig(level=logging.DEBUG, format=log_format)
        # logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger('Daily coding - problem 0001 - 2sum')
        self.counters = {}

    def do_run(self, nums: list[int], sum_value: int, expected: bool) -> None:
        deltas = []
        for i in range(100):
            start = time.perf_counter()
            result = check_if_sum_exists(nums, sum_value)
            end = time.perf_counter()
            self.assertEqual(expected, result)  # add assertion here
            deltas.append(end - start)

        sample_size = len(nums)
        delta = mean(deltas)
        self.logger.info(f'Array Size: {sample_size:10}; ETA: {delta : .10f}')
        self.counters[sample_size] = delta

    def test_00004_true(self):
        nums = [10, 15, 3, 7]
        sum_value = 17
        self.do_run(nums, sum_value, True)

    def test_00004_false(self):
        nums = [10, 15, 3, 7]
        sum_value = 150
        self.do_run(nums, sum_value, False)

    def test_00100(self):
        nums = list(range(100))
        sum_value = nums[-1] + nums[-2]
        self.do_run(nums, sum_value, True)

    def test_01000(self):
        nums = list(range(1000))
        sum_value = nums[-1] + nums[-2]
        self.do_run(nums, sum_value, True)

    def test_02000(self):
        nums = list(range(2000))
        sum_value = nums[-1] + nums[-2]
        self.do_run(nums, sum_value, True)

    def test_04000(self):
        nums = list(range(4000))
        sum_value = nums[-1] + nums[-2]
        self.do_run(nums, sum_value, True)

    def test_08000(self):
        nums = list(range(8000))
        sum_value = nums[-1] + nums[-2]
        self.do_run(nums, sum_value, True)

    def test_16000(self):
        nums = list(range(16000))
        sum_value = nums[-1] + nums[-2]
        self.do_run(nums, sum_value, True)

    def test_32000(self):
        nums = list(range(32000))
        sum_value = nums[-1] + nums[-2]
        self.do_run(nums, sum_value, True)

    # def test_10000(self):
    #     nums = list(range(10000))
    #     sum_value = nums[-1] + nums[-2]
    #     self.do_run(nums, sum_value, True)


if __name__ == '__main__':
    unittest.main()
