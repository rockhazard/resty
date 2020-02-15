#!/usr/bin/env python3
"""
===============================================================================
A script that queries and reports REST status codes for given domain names.
License: MIT
Author: Ike Davis
===============================================================================
"""


import sys
import argparse
from textwrap import dedent
from requests import get, exceptions as reqx


class Resty(object):
    """domain querying class"""

    def __init__(self):
        super(Resty, self).__init__()
        self.domainsList = []
        self.codes = {
            100: 'Continue',
            101: 'Switching Protocols',
            102: 'Processing',
            103: 'Early Hints',
            200: 'OK',
            201: 'Created',
            202: 'Accepted',
            203: 'Non-Authoritative Information',
            204: 'No Content',
            205: 'Reset Content',
            206: 'Partial Content',
            300: 'Multiple Choices',
            301: 'Moved Permanently',
            302: 'Found',
            303: 'See Other',
            304: 'Not Modified',
            305: 'Use Proxy',
            306: 'Unused',
            307: 'Temporary Redirect',
            308: 'Permanent Redirect',
            400: 'Bad Request',
            401: 'Unauthorized',
            402: 'Payment Required',
            403: 'Forbidden',
            404: 'Not Found',
            405: 'Method Not Allowed',
            406: 'Not Acceptable',
            407: 'Proxy Authentication Required',
            408: 'Request Timeout',
            409: 'Conflict',
            410: 'Gone',
            411: 'Length Required',
            412: 'Precondition Failed',
            413: 'Request Entity Too Large',
            414: 'Request-URI Too Long',
            415: 'Unsupported Media Type',
            416: 'Requested Range Not Satisfiable',
            417: 'Expectation Failed',
            418: 'I\'m a teapot',
            421: 'Misdirected Request',
            422: 'Unprocessable Entity',
            423: 'Locked',
            425: 'Too Early',
            426: 'Upgrade Required',
            428: 'Precondition Required',
            429: 'Too Many Requests',
            431: 'Request Header Fields Too Large',
            451: 'Unavailable For Legal Reasons',
            500: 'Internal Server Error',
            501: 'Not Implemented',
            502: 'Bad Gateway',
            503: 'Service Unavailable',
            504: 'Gateway Timeout',
            505: 'HTTP Version Not Supported',
            506: 'Variant Also Negotiates',
            507: 'Insufficient Storage',
            511: 'Network Authentication Required',
            520: 'Web server is returning an unknown error',
            522: 'Connection timed out',
            524: 'A timeout occurred'}

    def get_urls(self, urls):
        with open(urls) as domains:
            # strip duplicate urls
            domainsSet = set(domains.read().splitlines())
            return list(domainsSet)

    def get_status_codes(self, urlList, timeout):
        msgList = []
        for url in urlList:
            try:
                code = get(url, timeout=timeout).status_code
                for status, message in self.codes.items():
                    if status == code:
                        # build list for later processing but print progress
                        msgList.append([code, url])
                        print('{}: {} - {}'.format(code, message, url))
            except KeyboardInterrupt:
                print('Program interrupted by user.')
                sys.exit(1)
            except reqx.SSLError:
                msgList.append(['SSL Error', url])
                print('ERR: SSL Error Detected: {}'.format(url))
                continue
            except reqx.MissingSchema:
                msgList.append(['Invalid URL', url])
                print('ERR: Invalid URL: {}'.format(url))
                continue
            except:
                print('ERR: No response: {}'.format(url))
                continue
        return msgList

    def get_1_code(self, url, timeout):
        try:
            code = get(url, timeout=timeout).status_code
        except reqx.SSLError:
            print('ERR: SSL Error Detected: {}'.format(url))
            sys.exit(1)
        except reqx.MissingSchema:
            print('ERR: Invalid URL: {}'.format(url))
            sys.exit(1)
        for status, message in self.codes.items():
            if status == code:
                return '{}: {} - {}'.format(code, message, url)


def main(*args):
    resty = Resty()

    """
    COMMANDLINE OPTIONS
    """
    parser = argparse.ArgumentParser(
        prog=sys.argv[0][2:], description=dedent("""\
            %(prog)s retrieves the HTTP REST status codes for given urls.
            The program reports these codes to the terminal for analysis.
            These source urls are taken from a return-separated list in a
            raw text file or from a single url typed at the terminal.

            The program also tests the SSL certificates for given urls.
            It will report SSL errors to the terminal as they occur.

            Fully qualified domain names and protocols are required, as in:
            https://www.example.org"""),
        epilog="""Author: (c) Ike Davis, 2020, License: MIT""")
    parser.add_argument('--version', help='print version info then exit',
                        version='%(prog)s v1.0 by Ike Davis MIT License',
                        action='version')
    parser.add_argument('-u', '--urls',
                        help='Report REST status codes for urls in URLS_FILE.',
                        nargs=1, metavar=('URLS_FILE'))
    parser.add_argument('-s', '--status',
                        help='Report the REST status code for a single url.',
                        nargs=1, metavar=('URL'))
    parser.add_argument('-t', '--timeout',
                        help='Set HTTP requests timeout in SECONDS (x[.x...]).',
                        nargs=1, metavar=('SECONDS'))

    args = parser.parse_args()
    if args.timeout:
        try:
            timeout = float(args.timeout[0])
        except ValueError as e:
            print(e)
            sys.exit(1)
    else:
        timeout = 0.5
    if args.urls:
        urls = resty.get_urls(args.urls[0])
        resty.get_status_codes(urls, timeout)
    elif args.status:
        print(resty.get_1_code(args.status[0], timeout))



if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))