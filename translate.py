#!/usr/bin/python

def lookahead(tokens):
  remain = tokens
  first = remain.pop(0)
  return [first, remain]

def parse_declaration(tokens):
  pass

def parse_while(tokens):
  pass

def parse_if(tokens):
  pass

def parse_assign(tokens):
  pass

def parse_print(tokens):
  
  res = ""

  while tokens[0] != "_NEWLINE":
    pass

def parse_statement:
  pass


def parse(tokens):

  res = ""

  while len(tokens) > 0:

    la = lookahead(tokens)

    if la[0] == "OUTPUT":

      res = res + "print"
      pp = parse_print(la[1])
      res = res + pp[0]
      tokens = pp[1]

  return res
