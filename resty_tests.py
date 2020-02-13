#!/usr/bin/env python3
# Python3 unit testing template


import unittest
from resty import Resty


class Test(unittest.TestCase):

    def setUp(self):
        self.Resty1 = Resty()

    def test_get_status_codes(self):
        result_get_status_codes = self.Resty1.get_status_codes(
            ['https://httpstat.us/200'])
        # assert result of tested method call
        self.assertEqual(result_get_status_codes, [[200, 'https://httpstat.us/200']], 'Not equal')

    def test_get_1_code(self):
        result_get_1_code = self.Resty1.get_1_code('https://httpstat.us/200')
        # assert result of tested method call
        self.assertEqual(result_get_1_code, '200: OK - https://httpstat.us/200', 'Not equal')


'''
ASSERTS:
self.assert - base assert allowing you to write your own assertions
self.assertEqual(a, b) - check a and b are equal
self.assertNotEqual(a, b) - check a and b are not equal
self.assertIn(a, b) - check that a is in the item b
self.assertNotIn(a, b) - check that a is not in the item b
self.assertFalse(a) - check that the value of a is False
self.assertTrue(a) - check the value of a is True
self.assertIsInstance(a, TYPE) - check that a is of type "TYPE"
self.assertRaises(ERROR, a, args) - check that when a is called with 
    args that it raises ERROR
'''

if __name__ == "__main__":
    # call unittest module
    unittest.main()
