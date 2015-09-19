#!/usr/bin/env python

import argparse

from login import login
from submit import submit as _submit
from uhunt import ac_count as _ac_count
from problem import write as _write
from problem import download_pdf as _download_pdf

def submit(args):
    s = login()
    _submit(s, args.problem, args.filename)

def ac_count(args):
    count = _ac_count(args.username)
    print args.username, count

def download_pdf(args):
    try:
        _download_pdf(args.problem)
    except Exception as e:
        print e

def write(args):
    _write(args.problem)

parser = argparse.ArgumentParser(description='A uva command line tool')
subparser = parser.add_subparsers()

p = subparser.add_parser('submit', help='submit problem')
p.add_argument('problem', help='problem id')
p.add_argument('-f', '--filename', help='filename')
p.set_defaults(func=submit)

p = subparser.add_parser('ac', help='ac count of user')
p.add_argument('username', help='username')
p.set_defaults(func=ac_count)

p = subparser.add_parser('pdf', help='download problem pdf')
p.add_argument('problem', help='problem id')
p.set_defaults(func=download_pdf)

p = subparser.add_parser('write', help='write problem')
p.add_argument('problem', help='problem id')
p.set_defaults(func=write)

args = parser.parse_args()

args.func(args)

