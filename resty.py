#!/usr/bin/env python3
"""
===============================================================================
A script that queries and reports REST status codes for given domain names.
===============================================================================
"""


# from textwrap import dedent
# from pathlib import fPath
import sys
import argparse
from requests import get
from time import sleep


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

    def get_status_codes(self, urlList):
        msgList = []
        for url in urlList:
            try:
                code = get(url, timeout=0.5).status_code
                for status, message in self.codes.items():
                    if status == code:
                        # build list for later processing but print progress
                        msgList.append([code, url])
                        print('{}: {} - {}'.format(code, message, url))
            except: 
                continue
        return msgList

    def get_1_code(self, url):
        code = get(url, timeout=0.5).status_code
        for status, message in self.codes.items():
            if status == code:
                return '{}: {} - {}'.format(code, message, url)


def main(*args):
    resty = Resty()

    """
    COMMANDLINE OPTIONS
    """
    parser = argparse.ArgumentParser(
        prog=sys.argv[0][2:], description="""%(prog)s description""",
        epilog="""Author: rockhazard License: MIT""")
    parser.add_argument('--version', help='print version info then exit',
                        version='%(prog)s v1.0 MIT License', action='version')
    # parser.add_argument('--foo', help='Help for --foo', action='store_true')
    parser.add_argument('-d', '--domains',
                        help='The locations of a text list of domains.',
                        nargs=1, metavar=('DOMAINS_FILE'))
    parser.add_argument('-s', '--status',
                        help='Get the REST status code for a single url.',
                        nargs=1, metavar=('URL'))

    args = parser.parse_args()

    if args.domains:
        urls = resty.get_urls(args.domains[0])
        resty.get_status_codes(urls)
    elif args.status:
        print(resty.get_1_code(args.status[0]))


if __name__ == "__main__":  # if not imported as module, execute script
    sys.exit(main(sys.argv[1:]))
