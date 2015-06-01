#!/usr/bin/python

from datetime import datetime
from pymongo import MongoClient
import sys, getopt, json

try:
  client = MongoClient()
except:
  print "Error establishing connection with mongo server."

def us(td):
  return (td.days * 24 * 60 * 60 + td.seconds) * 1000 * 1000 + td.microseconds

def bench_query_latency(queryfile, db_name, collection_name, repeat):
  db = client[db_name]
  collection = db[collection_name]
  qout = open('latency_results_regex', 'w')
  with open(queryfile) as ifp:
    qid = 0
    for line in ifp:
      query = line.strip()
      print "Query: (%s)" % query
      for i in range(0, repeat):
        count = 0
        start = datetime.now()
        results = collection.find({'text': { '$regex' : query }}, { '_id': 1 })
        for res in results:
          count += 1
        end = datetime.now()
        diff = end - start
        print "Query %d iteration %d completed; took %d microseconds for %ld documents" % (qid, i, us(diff), count)
        qout.write("%d\t%d\t%d\t%d\n" % (qid, i, count, us(diff)))
      qid += 1
  qout.close()
  print "Finished benchmarking."

def main(argv):
  queryfile = ''
  db = 'test'
  collection = 'test'
  repeat = 10
  try:
    opts, args = getopt.getopt(argv,"hq:d:c:r:",["qfile=","db=","collection=","repeat="])
  except getopt.GetoptError:
    print 'mongoperf.py -q <query-file> -d <database> -c <collection>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'mongoperf.py -q <query-file> -d <database> -c <collection> -r <repeat-count>'
      sys.exit()
    elif opt in ("-q", "--qfile"):
      queryfile = arg
    elif opt in ("-d", "--db"):
      db = arg
    elif opt in ("-c", "--collection"):
      collection = arg
    elif opt in ("-r", "--repeat"):
      repeat = int(arg)
  if queryfile == '':
  	print "Error: Must specify query-file!"
  	sys.exit(2)
  bench_query_latency(queryfile, db, collection, repeat)

if __name__ == "__main__":
   main(sys.argv[1:])
