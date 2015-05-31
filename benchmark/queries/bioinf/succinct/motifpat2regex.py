#!/usr/bin/python
import sys, getopt

alphabet = set('ACDEFGHIKLMNPQRSTVWY')

def motifpat2regex(motifpat):
  regex = ''
  i = 0
  while i < len(motifpat):
    if motifpat[i] == 'x':
      regex += '.'
      i += 1
    elif motifpat[i] == '(':
      prev_tok = str(regex[-1])
      regex = regex[:-1]
      rangebuf = ''
      i += 1
      while motifpat[i] != ')':
        rangebuf += motifpat[i]
        i += 1
      i += 1
      if ',' in rangebuf:
        regex += ('(' + prev_tok + '{' + rangebuf + '})')
      else:
        regex += prev_tok * int(rangebuf)
    elif motifpat[i] == '{':
       negbuf = ''
       i += 1
       while motifpat[i] != '}':
         negbuf += motifpat[i]
         i += 1
       i += 1
       regex += '[' + ''.join(alphabet - set(negbuf)) + ']'
    elif motifpat[i] != '.' and motifpat[i] != '-':
      regex += motifpat[i]
      i += 1
    else:
      i += 1
  return regex

def convert(inp, out):
  ofp = open(out,'w')
  with open(inp) as ifp:
    seq_buf = ''
    for line in ifp:
      motifpat = line.strip()
      ofp.write(motifpat2regex(motifpat + '\n'))
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
    print 'motifpat2regex.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  if outputfile == '':
    print "Must provide valid output file"
    print 'motifpat2regex.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  convert(inputfile, outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
