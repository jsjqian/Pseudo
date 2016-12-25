#!/usr/bin/python

import re
import sys

def tokenize(str):
  output = []
  tokens = str.split( )
  for token in tokens:
    output.append((re.sub(r'[!,\.\?;:]', '', token)).upper())
  print output

def main():
  if len(sys.argv) > 2:
    print "pseudo: " + " ".join(sys.argv) + ". Too many arguments. Usage: pseudo file"
    exit()
  elif len(sys.argv) < 2:
    print "pseudo: Too few arguments. Usage: pseudo file"
    exit()
  filename = sys.argv[1]
  f = open(filename, 'r')
  str = f.read()
  tokenize(str)

if __name__ == "__main__":
  main()
