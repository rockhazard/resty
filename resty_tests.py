#!/usr/bin/env python3
# Python3 unit testing template


import unittest
from textwrap import dedent
from unittest import mock

from resty import Resty


class RestyTest(unittest.TestCase):

    def setUp(self):
        self.Resty1 = Resty()
        self.code = mock.Mock(return_value=200)
        self.testUrls = [
            'https://httpstat.us/100',
            'https://httpstat.us/101',
            'https://httpstat.us/102',
            'https://httpstat.us/103',
            'https://httpstat.us/200',
            'https://httpstat.us/201',
            'https://httpstat.us/202',
            'https://httpstat.us/203',
            'https://httpstat.us/204',
            'https://httpstat.us/205',
            'https://httpstat.us/206',
            'https://httpstat.us/300',
            'https://httpstat.us/301',
            'https://httpstat.us/302',
            'https://httpstat.us/303',
            'https://httpstat.us/304',
            'https://httpstat.us/305',
            'https://httpstat.us/306',
            'https://httpstat.us/307',
            'https://httpstat.us/308',
            'https://httpstat.us/400',
            'https://httpstat.us/401',
            'https://httpstat.us/402',
            'https://httpstat.us/403',
            'https://httpstat.us/404',
            'https://httpstat.us/405',
            'https://httpstat.us/406',
            'https://httpstat.us/407',
            'https://httpstat.us/408',
            'https://httpstat.us/409',
            'https://httpstat.us/410',
            'https://httpstat.us/411',
            'https://httpstat.us/412',
            'https://httpstat.us/413',
            'https://httpstat.us/414',
            'https://httpstat.us/415',
            'https://httpstat.us/416',
            'https://httpstat.us/417',
            'https://httpstat.us/418',
            'https://httpstat.us/421',
            'https://httpstat.us/422',
            'https://httpstat.us/423',
            'https://httpstat.us/425',
            'https://httpstat.us/426',
            'https://httpstat.us/428',
            'https://httpstat.us/429',
            'https://httpstat.us/431',
            'https://httpstat.us/451',
            'https://httpstat.us/500',
            'https://httpstat.us/501',
            'https://httpstat.us/502',
            'https://httpstat.us/503',
            'https://httpstat.us/504',
            'https://httpstat.us/505',
            'https://httpstat.us/506',
            'https://httpstat.us/507',
            'https://httpstat.us/511',
            'https://httpstat.us/520',
            'https://httpstat.us/522',
            'https://httpstat.us/524'
        ]
        self.urls_source = dedent("""\
            https://httpstat.us/100\n\
            https://httpstat.us/101\n\
            https://httpstat.us/102\n\
            https://httpstat.us/103\n\
            https://httpstat.us/200\n\
            https://httpstat.us/201\n\
            https://httpstat.us/202\n\
            https://httpstat.us/203\n\
            https://httpstat.us/204\n\
            https://httpstat.us/205\n\
            https://httpstat.us/206\n\
            https://httpstat.us/300\n\
            https://httpstat.us/301\n\
            https://httpstat.us/302\n\
            https://httpstat.us/303\n\
            https://httpstat.us/304\n\
            https://httpstat.us/305\n\
            https://httpstat.us/306\n\
            https://httpstat.us/307\n\
            https://httpstat.us/308\n\
            https://httpstat.us/400\n\
            https://httpstat.us/401\n\
            https://httpstat.us/402\n\
            https://httpstat.us/403\n\
            https://httpstat.us/404\n\
            https://httpstat.us/405\n\
            https://httpstat.us/406\n\
            https://httpstat.us/407\n\
            https://httpstat.us/408\n\
            https://httpstat.us/409\n\
            https://httpstat.us/410\n\
            https://httpstat.us/411\n\
            https://httpstat.us/412\n\
            https://httpstat.us/413\n\
            https://httpstat.us/414\n\
            https://httpstat.us/415\n\
            https://httpstat.us/416\n\
            https://httpstat.us/417\n\
            https://httpstat.us/418\n\
            https://httpstat.us/421\n\
            https://httpstat.us/422\n\
            https://httpstat.us/423\n\
            https://httpstat.us/425\n\
            https://httpstat.us/426\n\
            https://httpstat.us/428\n\
            https://httpstat.us/429\n\
            https://httpstat.us/431\n\
            https://httpstat.us/451\n\
            https://httpstat.us/500\n\
            https://httpstat.us/501\n\
            https://httpstat.us/502\n\
            https://httpstat.us/503\n\
            https://httpstat.us/504\n\
            https://httpstat.us/505\n\
            https://httpstat.us/506\n\
            https://httpstat.us/507\n\
            https://httpstat.us/511\n\
            https://httpstat.us/520\n\
            https://httpstat.us/522\n\
            https://httpstat.us/524\n""")

        self.codes = [
            100,
            101,
            102,
            103,
            200,
            201,
            202,
            203,
            204,
            205,
            206,
            300,
            301,
            302,
            303,
            304,
            305,
            306,
            307,
            308,
            400,
            401,
            402,
            403,
            404,
            405,
            406,
            407,
            408,
            409,
            410,
            411,
            412,
            413,
            414,
            415,
            416,
            417,
            418,
            421,
            422,
            423,
            425,
            426,
            428,
            429,
            431,
            451,
            500,
            501,
            502,
            503,
            504,
            505,
            506,
            507,
            511,
            520,
            522,
            524
        ]

        self.messages = [
            'Continue',
            'Switching Protocols',
            'Processing',
            'Early Hints',
            'OK',
            'Created',
            'Accepted',
            'Non-Authoritative Information',
            'No Content',
            'Reset Content',
            'Partial Content',
            'Multiple Choices',
            'Moved Permanently',
            'Found',
            'See Other',
            'Not Modified',
            'Use Proxy',
            'Unused',
            'Temporary Redirect',
            'Permanent Redirect',
            'Bad Request',
            'Unauthorized',
            'Payment Required',
            'Forbidden',
            'Not Found',
            'Method Not Allowed',
            'Not Acceptable',
            'Proxy Authentication Required',
            'Request Timeout',
            'Conflict',
            'Gone',
            'Length Required',
            'Precondition Failed',
            'Request Entity Too Large',
            'Request-URI Too Long',
            'Unsupported Media Type',
            'Requested Range Not Satisfiable',
            'Expectation Failed',
            'I\'m a teapot',
            'Misdirected Request',
            'Unprocessable Entity',
            'Locked',
            'Too Early',
            'Upgrade Required',
            'Precondition Required',
            'Too Many Requests',
            'Request Header Fields Too Large',
            'Unavailable For Legal Reasons',
            'Internal Server Error',
            'Not Implemented',
            'Bad Gateway',
            'Service Unavailable',
            'Gateway Timeout',
            'HTTP Version Not Supported',
            'Variant Also Negotiates',
            'Insufficient Storage',
            'Network Authentication Required',
            'Web server is returning an unknown error',
            'Connection timed out',
            'A timeout occurred'
        ]

        self.msgList = [
            [100, 'Continue', 'https://httpstat.us/100'],
            [101, 'Switching Protocols', 'https://httpstat.us/101'],
            [102, 'Processing', 'https://httpstat.us/102'],
            [103, 'Early Hints', 'https://httpstat.us/103'],
            [200, 'OK', 'https://httpstat.us/200'],
            [201, 'Created', 'https://httpstat.us/201'],
            [202, 'Accepted', 'https://httpstat.us/202'],
            [203, 'Non-Authoritative Information', 'https://httpstat.us/203'],
            [204, 'No Content', 'https://httpstat.us/204'],
            [205, 'Reset Content', 'https://httpstat.us/205'],
            [206, 'Partial Content', 'https://httpstat.us/206'],
            [300, 'Multiple Choices', 'https://httpstat.us/300'],
            [301, 'Moved Permanently', 'https://httpstat.us/301'],
            [302, 'Found', 'https://httpstat.us/302'],
            [303, 'See Other', 'https://httpstat.us/303'],
            [304, 'Not Modified', 'https://httpstat.us/304'],
            [305, 'Use Proxy', 'https://httpstat.us/305'],
            [306, 'Unused', 'https://httpstat.us/306'],
            [307, 'Temporary Redirect', 'https://httpstat.us/307'],
            [308, 'Permanent Redirect', 'https://httpstat.us/308'],
            [400, 'Bad Request', 'https://httpstat.us/400'],
            [401, 'Unauthorized', 'https://httpstat.us/401'],
            [402, 'Payment Required', 'https://httpstat.us/402'],
            [403, 'Forbidden', 'https://httpstat.us/403'],
            [404, 'Not Found', 'https://httpstat.us/404'],
            [405, 'Method Not Allowed', 'https://httpstat.us/405'],
            [406, 'Not Acceptable', 'https://httpstat.us/406'],
            [407, 'Proxy Authentication Required', 'https://httpstat.us/407'],
            [408, 'Request Timeout', 'https://httpstat.us/408'],
            [409, 'Conflict', 'https://httpstat.us/409'],
            [410, 'Gone', 'https://httpstat.us/410'],
            [411, 'Length Required', 'https://httpstat.us/411'],
            [412, 'Precondition Failed', 'https://httpstat.us/412'],
            [413, 'Request Entity Too Large', 'https://httpstat.us/413'],
            [414, 'Request-URI Too Long', 'https://httpstat.us/414'],
            [415, 'Unsupported Media Type', 'https://httpstat.us/415'],
            [416, 'Requested Range Not Satisfiable', 'https://httpstat.us/416'],
            [417, 'Expectation Failed', 'https://httpstat.us/417'],
            [418, 'I\'m a teapot', 'https://httpstat.us/418'],
            [421, 'Misdirected Request', 'https://httpstat.us/421'],
            [422, 'Unprocessable Entity', 'https://httpstat.us/422'],
            [423, 'Locked', 'https://httpstat.us/423'],
            [425, 'Too Early', 'https://httpstat.us/425'],
            [426, 'Upgrade Required', 'https://httpstat.us/426'],
            [428, 'Precondition Required', 'https://httpstat.us/428'],
            [429, 'Too Many Requests', 'https://httpstat.us/429'],
            [431, 'Request Header Fields Too Large', 'https://httpstat.us/431'],
            [451, 'Unavailable For Legal Reasons', 'https://httpstat.us/451'],
            [500, 'Internal Server Error', 'https://httpstat.us/500'],
            [501, 'Not Implemented', 'https://httpstat.us/501'],
            [502, 'Bad Gateway', 'https://httpstat.us/502'],
            [503, 'Service Unavailable', 'https://httpstat.us/503'],
            [504, 'Gateway Timeout', 'https://httpstat.us/504'],
            [505, 'HTTP Version Not Supported', 'https://httpstat.us/505'],
            [506, 'Variant Also Negotiates', 'https://httpstat.us/506'],
            [507, 'Insufficient Storage', 'https://httpstat.us/507'],
            [511, 'Network Authentication Required', 'https://httpstat.us/511'],
            [520, 'Web server is returning an unknown error', 'https://httpstat.us/520'],
            [522, 'Connection timed out', 'https://httpstat.us/522'],
            [524, 'A timeout occurred', 'https://httpstat.us/524']
        ]

    """tests for get_status_codes"""

    def test_get_status_codes(self):
        """test msgList build"""
        self.Resty1._state['quiet'] = True
        codes = iter(self.codes)
        result_get_status_codes = self.Resty1.get_status_codes(
            self.testUrls, timeout=0.0002, iter_codes=codes)
        # assert result of tested method call
        self.assertEqual(result_get_status_codes, self.msgList, 'Not equal')

    """tests for get_1_code"""

    def test_get_1_code(self):
        """test single line message formatting"""
        result_get_1_code = self.Resty1.get_1_code(
            'https://httpstat.us/200', timeout=0.0002, code=self.code)
        # assert result of tested method call
        self.assertEqual(result_get_1_code,
                         '200: OK - https://httpstat.us/200', 'Not equal')

    """tests for get_urls"""

    def test_get_urls(self):
        """test file parsing into per-line list"""
        with mock.patch('builtins.open', mock.mock_open(read_data=self.urls_source)):
            with open('/dev/null') as f:
                # print('contents of file from the mock patch: ' + f.read())
                result_test_get_urls = self.Resty1.get_urls(f)
                # function returns a set that is sorted for testing
                self.assertEqual(sorted(result_test_get_urls), self.testUrls, 'Not equal')

    """tests for time_proc"""

    def test_time_proc(self):
        """test time formatting"""
        self.Resty1._state['quiet'] = False
        result_test_time_proc = self.Resty1.time_proc(4200)
        self.assertEqual(result_test_time_proc, [[1, 10], 'Finished in 1:10:0'], 'Not equal')

    """tests for generate_report"""

    def test_generate_report(self):
        """test file formatting"""
        # result_generate_report = self.Resty1.ggenerate_report(self.msgList)
        # self.assertEqual(result_test_generate_report, 'result_output', 'Not equal')
        pass


if __name__ == "__main__":
    # call unittest module
    unittest.main()
