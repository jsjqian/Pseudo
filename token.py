#!/usr/bin/python

import re
import sys

def tokenize(file):
  tokens = []
  chars = read_by_char(file)
  words = clean(form_words(chars))
  for word in words:
    tokens.append((re.sub(r'[!,\.\?;:]', '', word)).upper())
  return tokens 

def read_by_char(file):
  ret = []
  while True:
    c = file.read(1)
    if not c:
      break
    ret.append(c)
  return ret

def form_words(chars):
  ret = []
  buffer = []
  count = 0;
  for c in chars:
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
      del buffer[:]
      ret.append('"')
    else: 
      buffer.append(c)
  ret.append(''.join(buffer))
  return ret

def clean(words):
  ret = []
  for w in words:
    if w != '':
      ret.append(w)
  return ret
