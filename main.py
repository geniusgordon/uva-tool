#!/usr/bin/env python

import argparse

from login import login
from submit import submit as _submit
from uhunt import ac_count as _ac_count

def submit(args):
    s = login()
    _submit(s, args.problem, args.filename)

def ac_count(args):
    count = _ac_count(args.username)
    print args.username, count

parser = argparse.ArgumentParser(description='A uva command line tool')
subparser = parser.add_subparsers()

p = subparser.add_parser('submit', help='submit problem')
p.add_argument('problem', help='problem id')
p.add_argument('-f', '--filename', help='filename')
p.set_defaults(func=submit)

p = subparser.add_parser('ac', help='ac count of user')
p.add_argument('username', help='username')
p.set_defaults(func=ac_count)

args = parser.parse_args()

args.func(args)

