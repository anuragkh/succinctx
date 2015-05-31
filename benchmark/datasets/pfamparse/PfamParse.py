#!/usr/bin/python

import sys, getopt

def parse(inp, out):
  ofp = open(out,'w')
  with open(inp) as ifp:
    seq_buf = ''
    for line in ifp:
      if line.startswith('>'):
        ofp.write(seq_buf + '\n')
        ofp.write(line)
        seq_buf = ''
      else:
        seq_buf += line.strip()
  ofp.close()

def main(argv):
  inputfile = ''
  outputfile = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print 'PfamParse.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
  if inputfile == '':
    print "Must provide valid input file"
    print 'PfamParse.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  if outputfile == '':
    print "Must provide valid output file"
    print 'PfamParse.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  parse(inputfile, outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
