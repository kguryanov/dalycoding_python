import unittest

from day00005_closures.impl.closures import car, cons, cdr


class MyTestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(car(cons(3, 4)), 3)  # add assertion here

    def test_second(self):
        self.assertEqual(cdr(cons(3, 4)), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
