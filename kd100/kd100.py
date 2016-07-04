#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

try:
    # py2
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib import urlencode
except ImportError:
    # py3
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode

import os
import json
import random
import argparse

GUESS = 'http://m.kuaidi100.com/autonumber/auto?{0}'
QUERY = 'http://m.kuaidi100.com/query?{0}'


def format_info(data):
    res = 'code: {nu: <20} company: {com: <15} ' \
          'is checked: {ischeck}\n'.format(**data)
    res += '=' * 65 + '\n'
    res += '{0: ^21}|{1: ^44}\n'.format('time', 'content')
    for item in data['data']:
        res += '-' * 65 + '\n'
        res += '{time: ^21}| {context}\n'.format(**item)
    res += '=' * 65 + '\n'
    return res


def kd100_query(code, output=None, quite=False, company=None):
    params = urlencode({'num': code})
    guess_url = GUESS.format(params)

    if company is None:
        res = json.loads(urlopen(guess_url).read().decode('utf-8'))
        possible_company_name = [company['comCode'] for company in res]
    else:
        possible_company_name = [str(company)]

    if not quite:
        print('Possible company:', ', '.join(possible_company_name))

    for company_name in possible_company_name:
        if not quite:
            print('Try', company_name, '...', end='')

        params = urlencode({
            'type': company_name,
            'postid': code,
            'id': 1,
            'valicode': '',
            'temp': random.random()
        })

        req = Request(QUERY.format(params), headers={'Referer': guess_url})
        res = json.loads(urlopen(req).read().decode('utf-8'))

        if res['message'] == 'ok':
            if not quite:
                print('Done.\n')
            table = format_info(res)
            if output:
                with open(output, 'wb') as f:
                    f.write(table.encode('utf-8'))
                if not quite:
                    print('Result saved to [' + os.path.abspath(output) + '].')
            else:
                print(table)
            break
        else:
            if not quite:
                print('Failed.')
    else:
        print('\nNo results.')


def main():
    parser = argparse.ArgumentParser(
        description="query express info use kuaidi100 api")
    parser.add_argument('-c', '--code', type=int, help='express code')
    parser.add_argument('-p', '--company', type=str,
                        help='express company, will auto '
                             'guess company if not provided',
                        default=None)
    parser.add_argument('-o', '--output', help='output file')
    parser.add_argument('-q', '--quite',
                        help='be quite',
                        action='store_true',
                        default=False)
    args = parser.parse_args()

    express_code = args.code
    if express_code is None:
        while True:
            try:
                express_code = int(input(
                    'Input your express code: ' if not args.quite else ''))
                break
            except ValueError:
                if not args.quite:
                    print('Please input a number')

    kd100_query(express_code, args.output, args.quite, args.company)

if __name__ == '__main__':
    main()
