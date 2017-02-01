#!/usr/bin/python

import token_string
import translate
import sys
import re

def main():

  if len(sys.argv) > 2:
    print "pseudo: " + " ".join(sys.argv) + ". Too many arguments. Usage: pseudo file"
    exit()
  #elif len(sys.argv) < 2:
    #print "pseudo: Too few arguments. Usage: pseudo file"
    #exit()

  #filename = sys.argv[1]
  #if re.match(r'(.*)\.psu$', filename) == None:
    #print "pseudo: Not a '.psu' file. Usage: pseudo file"
    #exit()

  #f = open(filename, 'r')
  str = ""
  for line in sys.stdin:
    str = str + line

  tokens = token_string.tokenize(str)
  translation = translate.parse(tokens)
  #f.close()
  code = open("translated_code" + '.py', 'w+')
  code.write(translation)
  code.close()
  exec(translation)
  print "Code has been run and has been translated into " + "translated_code" + ".py"

if __name__ == "__main__":
  main()
