#!/usr/bin/python

import sys, getopt, json

def tanl2json(inp, out):
  ofp = open(out,'w')
  with open(inp) as ifp:
    line_no = 0

    wiki_id = ''
    wiki_url = ''
    wiki_title = ''
    wiki_text = ''
    for line in ifp:
      if line_no % 3 == 0:
        header = line.strip()
        header = header[header.find('"') + 1:]
        wiki_id = header[:header.find('"')].encode('ascii', 'ignore')
        header = header[header.find('"') + 1:]
        wiki_url = header[:header.find('"')].encode('ascii', 'ignore')
        header = header[header.find('"') + 1:]
        wiki_title = header[:header.find('"')].encode('ascii', 'ignore')
        print wiki_id
        print wiki_url
        print wiki_title
      elif line_no % 3 == 1:
        wiki_text = line.strip()
      elif line_no % 2 == 2:
        article = dict(id=wiki_id, url=url, title=wiki_title, text=wiki_text)
        #ofp.write(json.dumps(article, encoding='utf-8') + '\n')
        wiki_id = ''
        wiki_url = ''
        wiki_title = ''
        wiki_text = ''
      line_no += 1
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
  tanl2json(inputfile, outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])