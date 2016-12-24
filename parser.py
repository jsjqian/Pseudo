#!/usr/bin/python

import re

def tokenize(input):
  output = []
  tokens = input.split( )
  for token in tokens:
    output.append((re.sub(r'[!,\.\?;:]', '', token)).upper())
  print output

def main():
  input = "Hello World!"
  tokenize(input)

if __name__ == "__main__":
  main()

