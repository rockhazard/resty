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

if __name__ == "__main__":
    # call unittest module
    unittest.main()
