#!/usr/bin/python

def lookahead(tokens):
  remain = tokens[:]
  first = remain.pop(0)
  return [first, remain]

def parse_while(ln, tokens):

  res = ""

  pe = parse_expression(ln, tokens)
  res = res + "while " + pe + ':'
  return res

def parse_for(ln, tokens):

  res = "for "

  la = lookahead(tokens)

  if la[0] == 'EACH':
    la = lookahead(la[1])
    res = res + la[0] + ' '
    la = lookahead(la[1])
    if la[0] == 'FROM':
      la = lookahead(la[1])
      if la[0] == '_NUMBER' or la[0] == '_VARIABLE':
        la = lookahead(la[1])
        start = la[0]
        la = lookahead(la[1])
        if la[0] == 'TO':
          la = lookahead(la[1])
          if la[0] == '_NUMBER' or la[0] == '_VARIABLE':
            la = lookahead(la[1])
            end = la[0]
            la = lookahead(la[1])
            if la[0] == 'COUNTING':
              la = lookahead(la[1])
              if la[0] == 'BY':
                la = lookahead(la[1])
                if la[0] == '_NUMBER' or la[0] == '_VARIABLE':
                  la = lookahead(la[1])
                  value = la[0]
                  res = res + "in range(" + start + ',' + end + ',' + value + '):'
                  return res
                else:
                  raise SyntaxError('line ' + ln + ': for declaration error')
              else:
                raise SyntaxError('line ' + ln + ': for declaration error')
            else:
              raise SyntaxError('line ' + ln + ': for declaration error')
          else:
            raise SyntaxError('line ' + ln + ': for declaration error')
        else:
          raise SyntaxError('line ' + ln + ': for declaration error')
      else:
        raise SyntaxError('line ' + ln + ': for declaration error')
    elif la[0] == 'IN':
      la = lookahead(la[1])
      res = res + "in " + la[0]
      return res
    else:
      raise SyntaxError('line ' + ln + ': for declaration error')
  else:
    raise SyntaxError('line ' + ln + ': for declaration error')

  return res

def parse_if(ln, tokens):

  res = ""

  la = lookahead(tokens)

  if la[0] == 'IF':

    res = res + "if "
    pe = parse_expression(ln, la[1])
    res = res + pe + ':'

  elif la[0] == 'ELSE':

    if len(la[1]) > 0 and la[1][0] == 'IF':
      la = lookahead(la[1])
      res = res + "elif "
      pe = parse_expression(ln, la[1])
      res = res + pe + ':'
    else:
      res = res + "else: "
  else:
    raise SyntaxError('line ' + ln + ': error with if statement')

  return res

def parse_assign(ln, tokens):

  res = ""

  la = lookahead(tokens)

  if la[0] == 'VARIABLE':
    la = lookahead(la[1])
    res = res + la[0] + ' = '
    la = lookahead(la[1])
    if la[0] == 'TO':
      pe = parse_expression(ln, la[1])
      res = res + pe
      return res
    else:
      raise SyntaxError('line ' + ln + ': assignment error')
  else:
    raise SyntaxError('line ' + ln + ': not an assignment')

def parse_variable(ln, tokens):

  res = ""

  la = lookahead(tokens)
  res = res + la[0] + ' '
  tokens = la[1]
  return [res, tokens]


def parse_print(ln, tokens):

  res = "print "

  pe = parse_expression(ln, tokens)
  res = res + pe

  return res

def parse_function(ln, tokens):

  res = "def "

  la = lookahead(tokens)

  if la[0] == 'FUNCTION':
    la = lookahead(la[1])
    res = res + la[0]
  else:
    raise SyntaxError('line ' + ln + ': improper function declaration')

  la = lookahead(la[1])

  if la[0] == 'TAKING':

    res = res + '('
    la = lookahead(la[1])

    while len(la[1]) > 0:
      if la[0] == 'VOID':
        break

      res = res + la[0]
      la = lookahead(la[1])

      if la[0] == 'AS':
        break
      else:
        res = res + ','

    res = res + '):'
    return res
  else:
    raise SyntaxError('line ' + ln + ': improper function declaration')

def parse_call(ln, tokens):

  res = ""

  la = lookahead(tokens)

  res = res + la[0]

  la = lookahead(la[1])

  if la[0] == 'WITH':

    res = res + '('
    la = lookahead(la[1])

    while len(la[1]) > 0:
      if la[0] == 'VOID':
        la = lookahead(la[1])
        break

      res = res + la[0]
      la = lookahead(la[1])

      if la[0] == 'NOW':
        break
      else:
        res = res + ','

    res = res + ')'
    tokens = la[1]
    return [res, tokens]
  else:
    raise SyntaxError('line ' + ln + ': improper function call')

def parse_string(ln, tokens):

  res = ""

  la = lookahead(tokens)

  if la[0] == '_STRING':
    string = lookahead(la[1])
    res = res + string[0]
    tokens = string[1]
    return [res, tokens]
  else:
    raise SyntaxError('line ' + ln + ': not a string')

def parse_number(ln, tokens):

  res = ""

  la = lookahead(tokens)

  if la[0] == '_NUMBER':
    number = lookahead(la[1])
    res = res + number[0] + ' '
    tokens = number[1]
    return [res, tokens]
  else:
    raise SyntaxError('line ' + ln + ': not a number')

def parse_expression(ln, tokens):

  res = ""

  while len(tokens) > 0:

    la = lookahead(tokens)

    if la[0] == '_STRING':
      ps = parse_string(ln, tokens)
      res = res + ps[0]
      tokens = ps[1]
    elif la[0] == "CALL":
      pc = parse_call(ln, la[1])
      res = res + pc[0]
      tokens = pc[1]
    elif la[0] == "VARIABLE":
      pv = parse_variable(ln, la[1])
      res = res + pv[0]
      tokens = pv[1]
    elif la[0] == '_NUMBER':
      pn = parse_number(ln, tokens)
      res = res + pn[0]
      tokens = pn[1]
    else:
      po = parse_operator(ln, tokens)
      res = res + po[0]
      tokens = po[1]

  return res

def parse_operator(ln, tokens):

  res = ""

  la = lookahead(tokens)

  if la[0] == 'AND':

    res = res + "and "
    return [res, la[1]]

  elif la[0] == 'OR':

    res = res + "or "
    return [res, la[1]]

  elif la[0] == 'PLUS':

    res = res + "+ "
    return [res, la[1]]

  elif la[0] == 'MINUS':

    res = res + "- "
    return [res, la[1]]

  elif la[0] == 'TIMES':

    res = res + "* "
    return [res, la[1]]

  elif la[0] == 'DIVIDES':

    res = res + "/ "
    return [res, la[1]]

  elif la[0] == 'REMAINDER':

    res = res + "% "
    return [res, la[1]]

  elif la[0] == 'GREATER':

    la = lookahead(la[1])
    if la[0] == 'THAN':
      la = lookahead(la[1])
      if la[0] == 'OR':
        la = lookahead(la[1])
        if la[0] == 'EQUAL':
          la = lookahead(la[1])
          if la[0] == "TO":
            res = res + ">= "
            return [res, la[1]]
          else:
            raise SyntaxError('line ' + ln + ': logical operator malformed')
        else:
          raise SyntaxError('line ' + ln + ': logical operator malformed')
      else:
        res = res + "> "
        return [res, [la[0]] + la[1]]
    else:
      raise SyntaxError('line ' + ln + ': logical operator malformed')

  elif la[0] == 'LESS':

    la = lookahead(la[1])
    if la[0] == 'THAN':
      la = lookahead(la[1])
      if la[0] == 'OR':
        la = lookahead(la[1])
        if la[0] == 'EQUAL':
          la = lookahead(la[1])
          if la[0] == "TO":
            res = res + "<= "
            return [res, la[1]]
          else:
            raise SyntaxError('line ' + ln + ': logical operator malformed')
        else:
          raise SyntaxError('line ' + ln + ': logical operator malformed')
      else:
        res = res + "< "
        return [res, [la[0]] + la[1]]
    else:
      raise SyntaxError('line ' + ln + ': logical operator malformed')

  elif la[0] == 'EQUALS':

    res = res + "== "
    return [res, la[1]]

  elif la[0] == 'NOT':

    la = lookahead(la[1])
    if la[0] == 'EQUALS':
      res = res + "!= "
      return [res, la[1]]

  else:
    raise SyntaxError('line ' + ln + ': parse operator error')

def parse(tokens):

  res = ""

  for i in range(0, len(tokens)):

    line = ""
    token = tokens[i]
    i = str(i + 1)
    la = lookahead(token)

    while la[0] == '_TAB':
      line = line + '\t'
      la = lookahead(la[1])

    if la[0] == "OUTPUT":

      print_statement = parse_print(i, la[1])
      line = line + print_statement
      res = res + line + '\n'

    elif la[0] == "SET":

      assign_statement = parse_assign(i, la[1])
      line = line + assign_statement
      res = res + line + '\n'

    elif la[0] == "MAKE":

      function_statement = parse_function(i, la[1])
      line = line + function_statement
      res = res + line + '\n'

    elif la[0] == "CALL":

      call_statement = parse_call(i, la[1])
      line = line + call_statement[0]
      res = res + line + '\n'

    elif la[0] == "IF" or la[0] == "ELSE":


      if_statement = parse_if(i, [la[0]] + la[1])
      line = line + if_statement
      res = res + line + '\n'

    elif la[0] == "WHILE":

      while_statement = parse_while(i, la[1])
      line = line + while_statement
      res = res + line + '\n'

    elif la[0] == "FOR":

      for_statement = parse_for(i, la[1])
      line = line + for_statement
      res = res + line + '\n'

    else:

      raise SyntaxError('line ' + i + ': error translating line')

  return res
