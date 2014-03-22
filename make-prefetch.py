#!/usr/bin/env python

from argparse import ArgumentParser
from hashlib import sha1, sha256
import os
import sys

usage = """make-prefetch.py [options] <file>

Create a prefetch statement for IBM Endpoint Manager ActionScript

Options:
  -a, --algorithm ALGORITHM    Hash algorithm to use (all, sha1, sha256)
                               default: all
  -o, --output OUTPUT          Output format (prefetch, davis, value)
                               default: prefetch
  -h, --help                   Print this help message and exit

Examples:
  Create a 9.1 style pretch statement

    make-prefetch.py hello.txt

  Create a 9.0 style prefetch statement

    make-prefetch.py --algorithm sha1 hello.txt

  Create a 7.2 style prefetch statement

    make-prefetch.py --algorithm sha1 --output davis hello.txt
"""

def hash(path):
  hashes = {}
  f = open(path, 'rb')
  contents = f.read()
  hashes['sha1'] = sha1(contents).hexdigest()
  hashes['sha256'] = sha256(contents).hexdigest()
  f.close()
  return hashes

def make_prefetch(file, algorithm):
  hashes = hash(file)  
  if algorithm == 'sha256':
    line = "prefetch {name} size:{size} http://REPLACEME sha256:{sha256}"
    return line.format(name=os.path.basename(file),
                       sha256=hashes['sha256'],
                       size=os.path.getsize(file))
  elif algorithm == 'sha1':
    line = "prefetch {name} sha1:{sha1} size:{size} http://REPLACEME"
    return line.format(name=os.path.basename(file),
                       sha1=hashes['sha1'],
                       size=os.path.getsize(file))
  else:
    line = ("prefetch {name} sha1:{sha1} size:{size} http://REPLACEME "
            "sha256:{sha256}")
    return line.format(name=os.path.basename(file),
                       sha1=hashes['sha1'],
                       sha256=hashes['sha256'],
                       size=os.path.getsize(file))

def make_value(file, algorithm):
  if algorithm == 'all':
    print("You must specify a hash algorithm to use")
    sys.exit(2)

  return hash(file)[algorithm]

def make_davis(file, algorithm):
  if algorithm != 'all' and algorithm != 'sha1':
    print("Algorithm {0} is not supported in davis downloads".format(algorithm))
    sys.exit(2)

  davis = """begin prefetch block
add prefetch item name={name} sha1={sha1} size={size} url=http://REPLACEME
collect prefetch items
end prefetch block"""
  return davis.format(name=os.path.basename(file),
                      sha1=hash(file)['sha1'],
                      size=os.path.getsize(file))

parser = ArgumentParser(description="Create a prefetch statement for "
                                    "IBM Endpoint Manager ActionScript",
                        add_help=False,
                        usage=usage)

parser.add_argument('file')

parser.add_argument(
  '-a',
  '--algorithm',
  choices=['all', 'sha1', 'sha256'],
  default='all')

parser.add_argument(
  '-o',
  '--output',
  choices=['value', 'davis', 'prefetch'],
  default='prefetch')

if '-h' in sys.argv or '--help' in sys.argv:
  print(usage)
  sys.exit()

args = parser.parse_args()

if args.output == 'value':
  print(make_value(args.file, args.algorithm))
elif args.output == 'davis':
  print(make_davis(args.file, args.algorithm))
else:
  print(make_prefetch(args.file, args.algorithm))
