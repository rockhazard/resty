#!/usr/bin/env python3
"""
===============================================================================
A script that queries URLs and reports REST status codes for given domain names.
Author: Ike Davis
License: MIT
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
        self._state = dict(quiet=False, stopwatch=False)
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

    def generate_report(self, data, filename):
        parent = str(Path(filename).parent)
        if Path(parent).exists():
            report = filename
        else:
            sys.exit('ERROR: report not written; file path does not exist.')

        with open(report, 'w', newline='', encoding='utf-8') as fn:
            if report.endswith('csv'):
                report_csv_writer = csv.writer(fn, delimiter=',',
                                               quotechar='\'', quoting=csv.QUOTE_MINIMAL)
                # csv column headers
                report_csv_writer.writerow(['Code'] + ['Message'] + ['URL'])
                for cell in data:
                    report_csv_writer.writerow(
                        [cell[0]] + [cell[1]] + [cell[2]])
            else:
                for line in data:
                    print('{}: \'{}\' - {}'.format(
                        str(line[0]), line[1], line[2]), file=fn, end='\n')

    def get_status_codes(self, urlList, timeout, iter_codes=False):
        for url in urlList:
            try:
                if iter_codes: # scaffold for test
                    code = next(iter_codes)

                else:
                    code = get(url, timeout=timeout).status_code
                for status, message in self.codes.items():
                    if status == code:
                        # build list for later processing but print progress
                        self.msgList.append([code, message, url])
                        if not self._state['quiet']:
                            print('{}: {} - {}'.format(code, message, url))
            except KeyboardInterrupt:
                sys.exit('Program interrupted by user.')
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
                    print('ERR: No Response: {}'.format(url))
                continue

        return self.msgList

    def get_1_code(self, url, timeout, code=False):
        try: # scaffold for test
            if code:
                code = code()
            else:
                code = get(url, timeout=timeout).status_code
        except reqx.SSLError:
            sys.exit('ERR: SSL Error Detected: {}'.format(url))
        except reqx.MissingSchema:
            sys.exit('ERR: Invalid URL: {}'.format(url))
        for status, message in self.codes.items():
            if status == code:
                return '{}: {} - {}'.format(code, message, url)


def main(*args):
    resty = Resty()

    """
    COMMANDLINE OPTIONS
    """
    parser = argparse.ArgumentParser(
        prog=Path(sys.argv[0][2:]).name, description=dedent("""\
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
                        version='%(prog)s v1.1 by Ike Davis MIT License',
                        action='version')
    parser.add_argument('-u', '--urls',
                        help='Output REST status codes to terminal for urls in URLS_FILE.',
                        nargs=1, metavar=('URLS_FILE'))
    parser.add_argument('-r', '--report',
                        help=dedent('Write REST status csv or raw text file to\
                         REPORT filename for urls in URLS_FILE. CSV or TXT format\
                          is determined by filename extension.'),
                        nargs=2, metavar=('URLS_FILE', 'REPORT'))
    parser.add_argument('-c', '--code',
                        help='Display the REST status code for a single url.',
                        nargs=1, metavar=('URL'))
    parser.add_argument('-t', '--timeout',
                        help='Set HTTP requests timeout in SECONDS (x[.x...]).',
                        nargs=1, metavar=('SECONDS'))
    parser.add_argument('-q', '--quiet',
                        help='Suppress output of progress to the terminal.',
                        action='store_true')
    parser.add_argument('-s', '--stopwatch',
                        help='Time the completion speed of the report.',
                        action='store_true')

    args = parser.parse_args()
    if args.stopwatch:
        resty.set_state('stopwatch', True)
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
    elif args.code:
        print(resty.get_1_code(args.status[0], timeout))
    elif args.report:
        urls = resty.get_urls(args.report[0])
        resty.get_status_codes(urls, timeout)
        resty.generate_report(resty.msgList, args.report[1])

    if resty.get_state('stopwatch'):
        end_timer = time()
        elapsed = end_timer - start_timer
        resty.time_proc(elapsed)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
