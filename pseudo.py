#!/usr/bin/python

import token
import translate
import sys
import re

def main():
  if len(sys.argv) > 2:
    print "pseudo: " + " ".join(sys.argv) + ". Too many arguments. Usage: pseudo file"
    exit()
  elif len(sys.argv) < 2:
    print "pseudo: Too few arguments. Usage: pseudo file"
    exit()
  filename = sys.argv[1]
  f = open(filename, 'r')
  tokens = token.tokenize(f)
  translation = translate.parse(tokens)
  code = open(

if __name__ == "__main__":
  main()
