#!/usr/bin/env python3
import interview

import unittest

class TestAsserts(unittest.TestCase):
    def setUp(self):
        pass # any setting up necessary

    def test_asserts(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertIn(1, range(10))
        self.assertIsInstance(2, int)
        self.assertAlmostEqual(2, 1.999999999)
        self.assertSetEqual({1,2,3},{3,2,1})
        self.assertListEqual([1,3,2],[1,3,2])

    def tearDown(self):
        pass # any tear down needed


class TestSquareMethod(unittest.TestCase):

    def test_int(self):
        self.assertEqual(3*3, interview.square(3))
        self.assertEqual(0*0, interview.square(0))
        self.assertEqual(-5*-5, interview.square(-5))

    def test_float(self):
        self.assertEqual(3.3*3.3, interview.square(3.3))
        self.assertEqual(0.0, interview.square(0.0))
        self.assertEqual(-3.14159*-3.14159, interview.square(-3.14159))

    def test_invalid(self):
        with self.assertRaisesRegex(Exception, "Invalid input type: type must be int or float"):
            interview.square("hello")
        with self.assertRaisesRegex(Exception, "Invalid input type: type must be int or float"):
            interview.square(True)


if __name__ == '__main__':
    unittest.main()


