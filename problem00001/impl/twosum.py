"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

Example: given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import logging


def check_if_sum_exists(numbers: list[int], expected: int) -> bool:
    remainders = set()
    for idx, val in enumerate(numbers):
        if (expected - val) in remainders:
            return True
        else:
            remainders.add(val)
    return False


def main() -> None:
    log_format = '%(levelname)s: %(asctime)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    logger = logging.getLogger()
    # logger.setLevel(logging.DEBUG)
    nums = [10, 15, 3, 7]
    expected = 17
    logger.info(f'Input: an array of {nums}, expected sum is {expected}')
    logger.info(f'The result is: {check_if_sum_exists(nums, expected)}')


if __name__ == '__main__':
    main()