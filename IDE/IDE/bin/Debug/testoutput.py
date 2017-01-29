import token
import translate
import sys
import re

def main():
  filename = sys.argv[1]
  f = open(filename, 'r')
  tokens = token.tokenize(f)
  translation = translate.parse(tokens)
  f.close()
  code = open(filename[:-4] + '.py', 'w+')
  code.write(translation)
  code.close()
  exec(translation)
  print "Code has been run and has been translated into " + filename[:-4] + ".py"

if __name__ == "__main__":
  main()
