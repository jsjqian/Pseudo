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

  while len(tokens) > 0:

    la = lookahead(tokens)

    if la[0] == 'STRING':
      string = lookahead(la[1])
      res = res + string[0]
      tokens = string[1]
    elif la[0] == "CALL":
      pass
    else:
      pe = parse_expression(tokens)
      res = res + pe[0]
      tokens = pe[1]

  return res
  
def parse_function(tokens):
  pass

def parse_expression(tokens):
  pass

def parse(tokens):

  res = ""

  for token in tokens:

    line = ""
    la = lookahead(token)

    if la[0] == "OUTPUT":

      line = line + "print "
      print_statement = parse_print(la[1])
      line = line + print_statement
      res = res + line

  return res
