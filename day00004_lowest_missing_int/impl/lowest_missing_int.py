"""
Given an array of integers, find the first missing positive integer in linear time and constant space.

In other words, find the lowest positive integer that does not exist in the array.

The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
import logging


def lowest_int_sorted(nums: list[int]) -> int:
    counter = 1
    for num in sorted(nums):
        if num <= 0:
            continue
        else:
            if num > counter:
                return counter
            else:
                counter += 1
    return counter


def lowest_int_set(nums: list[int]) -> int:
    if not nums:
        return 1
    nums_set = {num for num in nums if num > 0}
    counter = 1
    while counter in nums_set:
        counter += 1
    return counter


def lowest_int_sort_positives(nums: list[int]) -> int:
    if not nums:
        return 1

    for idx in range(len(nums)):
        while 0 < nums[idx] <= len(nums) and idx + 1 != nums[idx]:
            val = nums[idx]
            nums[idx], nums[val - 1] = nums[val - 1], nums[idx]
            if nums[idx] == nums[val - 1]:
                break

    for idx, val in enumerate(nums, 1):
        if val != idx:
            return idx

    return len(nums) + 1


def main():
    log_format = '%(levelname)s: %(asctime)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    logger = logging.getLogger()
    data = [3, 4, -1, 1]
    expected = 2
    logger.info(f'Data: {data}; expected result: 2')


if __name__ == '__main__':
    main()
