#!/usr/bin/python

import re
import sys

def tokenize(str):

  chars = read_by_char(str)
  words = clean(form_words(chars))
  lines = form_lines(words)
  tokens = lines

  return tokens 

def read_by_char(str):

  ret = []

  for i in range(0, len(str)):
    ret.append(str[i])

  ret.append('\n')

  return ret

def form_words(chars):

  ret = []
  buffer = []
  i = 0

  while i < len(chars):
    c = chars[i]
    if c == '\t':
      ret.append("_tab")
    elif c == ' ':
      word = ''.join(buffer)
      ret.append(word)
      del buffer[:]
    elif c == '\n':
      word = ''.join(buffer)
      ret.append(word)
      del buffer[:]
      ret.append("_newline")
    elif c == '"':
      word = ''.join(buffer)
      ret.append(word)
      ret.append("_string")
      del buffer[:]
      buffer.append(c)
      i = i + 1

      while chars[i] != '"':
        buffer.append(chars[i])
        i = i + 1

      buffer.append('"')
      word = ''.join(buffer)
      ret.append(word)
      del buffer[:]

    else: 
      buffer.append(c)

    i = i + 1

  ret.append(''.join(buffer))

  return ret

def clean(words):

  ret = []
  i = 0
  
  while i < len(words):
    w = words[i]
    if w != '':
      if w == "_string":
        ret.append(w.upper())
        i = i + 1
        ret.append(words[i])
      elif re.match( r'^-?\d*\.?\d+$', w):
        ret.append("_NUMBER")
        ret.append(words[i])
      else:
        ret.append((re.sub(r'[!\.\?;:]', '', w)).upper())
    i = i + 1

  return ret

def form_lines(words):

  ret = []
  buffer = []
  
  for word in words:
    if word == "_NEWLINE":
      line = buffer[:]
      ret.append(line)
      del buffer[:]
    else:
      buffer.append(word)

  return ret
