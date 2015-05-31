#!/usr/bin/python

import sys, getopt, json

def tanl2json(inp, out):
  ofp = open(out,'w')
  with open(inp) as ifp:

    wiki_id = ''
    wiki_url = ''
    wiki_title = ''
    wiki_text = ''
    for line in ifp:
      if '<doc' in line:
        header = line.strip()
        header = header[header.find('"') + 1:]
        wiki_id = header[:header.find('"')].decode('ascii', 'ignore')
        header = header[header.find('"') + 1:]
        header = header[header.find('"') + 1:]
        wiki_url = header[:header.find('"')].decode('ascii', 'ignore')
        header = header[header.find('"') + 1:]
        header = header[header.find('"') + 1:]
        wiki_title = header[:header.find('"')].decode('ascii', 'ignore')
      elif not ('</doc>' in line):
        wiki_text = line.strip()
        article = dict(_id=wiki_id, url=wiki_url, title=wiki_title, text=wiki_text)
        print "[%s] %s" % (wiki_id, wiki_title)
    	ofp.write(json.dumps(article, encoding='utf-8') + '\n')
    	wiki_id = ''
    	wiki_url = ''
    	wiki_title = ''
    	wiki_text = ''
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
