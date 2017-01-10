#!/usr/bin/python

def lookahead(tokens):
  remain = tokens
  first = remain.pop(0)
  return [first, remain]

def parse_variable(tokens):
  pass

def parse_print(tokens):
  pass

def parse(tokens):
  res = ""

  while len(tokens) > 0:
    la = lookahead(tokens)
    if la[0] == "OUTPUT":
      res = res + "print"

  return res
