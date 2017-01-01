#!/usr/bin/python

import token
import translate
import sys

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
  token.tokenize(str)

if __name__ == "__main__":
  main()
