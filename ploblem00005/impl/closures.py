"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.

Example 1:
    car(cons(3, 4)) returns 3,
    cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""
import logging


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    return pair(lambda a, b: a)


def cdr(pair):
    return pair(lambda a, b: b)


def main():
    log_format = '%(levelname)s: %(asctime)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    logger = logging.getLogger()
    logger.info(f'Result is: {car(cons(3, 4))}')


if __name__ == '__main__':
    main()
