#!/usr/bin/env python

import argparse

from login import login
from submit import submit

parser = argparse.ArgumentParser(description='A nthu ilms command line tool')
parser.add_argument('problem', help='problem id')
parser.add_argument('-f', '--filename', help='filename')

args = parser.parse_args()

s = login()
submit(s, args.problem, args.filename)

