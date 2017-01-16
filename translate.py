#!/usr/bin/python

def lookahead(tokens):
  remain = tokens[:]
  first = remain.pop(0)
  return [first, remain]

def parse_declaration(tokens):
  pass

def parse_while(tokens):
  pass

def parse_if(tokens):
  pass

def parse_assign(tokens):

  res = ""

  la = lookahead(tokens)

  if la[0] == 'SET':
    la = lookahead(la[1])
    if la[0] == 'VARIABLE':
      la = lookahead(la[1])
      res = res + la[0] + ' = '
      la = lookahead(la[1])
      if la[0] == 'TO':
        pe = parse_expression(la[1])
        res = res + pe
        return res
      else:
        raise SyntaxError('assignment error')
    else:
      raise SyntaxError('assignment error')
  else:
    raise SyntaxError('not an assignment')

def parse_print(tokens):
  
  res = "print "

  pe = parse_expression(tokens)
  res = res + pe

  return res
  
def parse_function(tokens):
  pass

def parse_string(tokens):

  res = ""

  la = lookahead(tokens)

  if la[0] == 'STRING':
    string = lookahead(la[1])
    res = res + string[0]
    tokens = string[1]
    return [res, tokens]
  else:
    raise SyntaxError('not a string')
  

def parse_expression(tokens):

  res = ""

  while len(tokens) > 0:

    la = lookahead(tokens)

    if la[0] == 'STRING':
      ps = parse_string(tokens)
      res = res + ps[0]
      tokens = ps[1]
    elif la[0] == "CALL":
      pass
    else:
      raise SyntaxError('invalid expression')

  return res

def parse(tokens):

  res = ""

  for token in tokens:

    line = ""
    la = lookahead(token)
    while la[0] == "_TAB":
      line = line + '\t'
      la = lookahead(la[1])

    if la[0] == "OUTPUT":

      print_statement = parse_print(la[1])
      line = line + print_statement
      res = res + line + '\n'

  return res
