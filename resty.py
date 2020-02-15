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
import os
import csv
from time import time
from pathlib import Path
from textwrap import dedent
from requests import get, exceptions as reqx


class Resty():
    """domain querying class"""

    def __init__(self):
        super(Resty, self).__init__()
        self._state = dict(quiet=False, timer=False)
        self.home = os.path.expanduser('~')
        self.msgList = []
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

    def set_state(self, key, value):
        self._state[key] = value

    def get_state(self, key):
        return self._state.get(key, None)

    def time_proc(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Finished in {0}:{1}:{2}".format(int(hours), int(mins), sec))

    def get_urls(self, urls):
        with open(urls) as domains:
            # strip duplicate urls
            domainsSet = set(domains.read().splitlines())
            return list(domainsSet)

    def generate_report(self, messages):
        csv_doc = str(Path(self.home, 'url_status_codes.csv'))
        with open(csv_doc.format(self.home), 'w', newline='') as csvfile:
            status_writer = csv.writer(csvfile, delimiter=',',
                                       quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            for message in messages:
                status_writer.writerow(
                    [message[0]] + [message[1]] + [message[2]])

    def get_status_codes(self, urlList, timeout):
        for url in urlList:
            try:
                code = get(url, timeout=timeout).status_code
                for status, message in self.codes.items():
                    if status == code:
                        # build list for later processing but print progress
                        self.msgList.append([code, message, url])
                        if not self._state['quiet']:
                            print('{}: {} - {}'.format(code, message, url))
            except KeyboardInterrupt:
                print('Program interrupted by user.')
                sys.exit(1)
            except reqx.SSLError:
                self.msgList.append(['ERR', 'SSL Error', url])
                if not self._state['quiet']:
                    print('ERR: SSL Error Detected: {}'.format(url))
                continue
            except reqx.MissingSchema:
                self.msgList.append(['ERR', 'Invalid URL', url])
                if not self._state['quiet']:
                    print('ERR: Invalid URL: {}'.format(url))
                continue
            except:
                if not self._state['quiet']:
                    print('ERR: No response: {}'.format(url))
                continue

        return self.msgList

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
            %(prog)s retrieves the HTTP REST status codes for given URLs.
            The program reports these codes to the terminal for analysis.
            These source URLs are taken from a return-separated list in a
            raw text file or from a single URL typed at the terminal.

            The program also tests the SSL certificates for given URLs.
            It will report SSL errors to the terminal as they occur.

            Valid URLs must contain the protocol and the fully qualified 
            domain name, as in: https://www.example.org"""),
        epilog="""Author: (c) Ike Davis, 2020, License: MIT""")
    parser.add_argument('--version', help='print version info then exit',
                        version='%(prog)s v1.0 by Ike Davis MIT License',
                        action='version')
    parser.add_argument('-u', '--urls',
                        help='Report REST status codes for urls in URLS_FILE.',
                        nargs=1, metavar=('URLS_FILE'))
    parser.add_argument('-r', '--report',
                        help='Write REST status csv for urls in URLS_FILE.',
                        nargs=1, metavar=('URLS_FILE'))
    parser.add_argument('-s', '--status',
                        help='Report the REST status code for a single url.',
                        nargs=1, metavar=('URL'))
    parser.add_argument('-t', '--timeout',
                        help='Set HTTP requests timeout in SECONDS (x[.x...]).',
                        nargs=1, metavar=('SECONDS'))
    parser.add_argument('-q', '--quiet',
                        help='Suppress output of progress to the terminal.',
                        action='store_true')
    parser.add_argument('-c', '--timer',
                        help='Time the completion speed of the report.',
                        action='store_true')

    args = parser.parse_args()
    if args.timer:
        resty.set_state('timer', True)
        start_timer = time()
    if args.quiet:
        resty.set_state('quiet', args.quiet)
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
    elif args.report:
        urls = resty.get_urls(args.report[0])
        resty.get_status_codes(urls, timeout)
        resty.generate_report(resty.msgList)

    if resty.get_state('timer'):
        end_timer = time()
        elapsed = end_timer - start_timer
        resty.time_proc(elapsed)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
