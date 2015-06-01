#!/usr/bin/python

from datetime import datetime
from elasticsearch import Elasticsearch
import sys, getopt, json

es = Elasticsearch()

def load_data(jsonfile, index, doc_type):
  doc_no = 1
  with open(jsonfile) as ifp:
    for line in ifp:
      doc = json.loads(line)
      if '_id' in doc:
        doc_id = doc['_id']
      else:
        doc_id = str(doc_no)
      res = es.index(index=index, doc_type=doc_type, id=doc_id, body=doc)
      print(res['created'])
      doc_no += 1

def main(argv):
  jsonfile = ''
  index = 'test'
  doc_type = 'test'
  try:
    opts, args = getopt.getopt(argv,"hj:i:t:",["ifile=","ofile="])
  except getopt.GetoptError:
    print 'esload.py -j <json-file> -i <index> -t <type>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'esload.py -j <json-file> -i <index> -t <type>'
      sys.exit()
    elif opt in ("-j", "--json"):
      jsonfile = arg
    elif opt in ("-i", "--index"):
      index = arg
    elif opt in ("-t", "--type"):
      doc_type = arg
  if jsonfile == '':
  	print "Error: Must specify json-file!"
  	sys.exit(2)
  load_data(jsonfile, index, doc_type)

if __name__ == "__main__":
   main(sys.argv[1:])