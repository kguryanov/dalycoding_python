"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
import logging
import numpy as np


def with_division(nums: list[int]) -> list[int]:
    """ Calculates an array containing products of all elements excedp the i-th element in original array
    :param nums: Input array
    :type nums: list[int]

    :returns: list[int]
    """
    multiple = np.prod(nums)

    return [multiple // i for i in nums]


def no_division(nums: list[int]) -> list[int]:
    forward = []
    backward = []
    result = []

    for num in nums:
        if forward:
            forward.append(forward[-1] * num)
        else:
            forward.append(num)

    for num in reversed(nums):
        if backward:
            backward.append(backward[-1] * num)
        else:
            backward.append(num)

    backward.reverse()

    for idx in range(len(nums)):
        if idx == 0:
            result.append(backward[idx + 1])
        elif idx == len(nums) - 1:
            result.append(forward[idx - 1])
        else:
            result.append(forward[idx - 1] * backward[idx + 1])

    return result


def main() -> None:
    log_format = '%(levelname)s: %(asctime)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    logger = logging.getLogger()
    # logger.setLevel(logging.DEBUG)
    nums = [1, 2, 3, 4, 5]
    expected = [120, 60, 40, 30, 24]
    logger.info(f'Input: an array of {nums}, expected array is {expected}')
    logger.info(f'The result with division is: {with_division(nums)}')
    logger.info(f'The result with no division is: {no_division(nums)}')


if __name__ == '__main__':
    main()
