# Benchmarking MongoDB

## Setting up EC2 instance

Start an r3.4xlarge instance; use following steps to install mongodb:

'''
sudo yum -y update

echo "[MongoDB]
name=MongoDB Repository
baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86\_64
gpgcheck=0
enabled=1" | sudo tee -a /etc/yum.repos.d/mongodb.repo

sudo yum install -y mongodb-org-server mongodb-org-mongos mongodb-org-shell mongodb-org-tools

sudo chkconfig mongod off

mkdir ~/configdb ~/data0 ~/data1 ~/data2 ~/data3 ~/data4 ~/data5 ~/data6 ~/data7

mongod --configsvr --fork --syslog --dbpath ~/configdb --port 27019

mongos --fork --syslog --configdb localhost --port 27017

mongod --fork --syslog --dbpath ~/data0 --port 27020

mongod --fork --syslog --dbpath ~/data1 --port 27021

mongod --fork --syslog --dbpath ~/data2 --port 27022

mongod --fork --syslog --dbpath ~/data3 --port 27023

mongod --fork --syslog --dbpath ~/data4 --port 27024

mongod --fork --syslog --dbpath ~/data5 --port 27025

mongod --fork --syslog --dbpath ~/data6 --port 27026

mongod --fork --syslog --dbpath ~/data7 --port 27027
'''

Now connect all the 'mongod' instances to the 'monogos' instance, and enable
sharding for the database and collection:

'''
mongo --port 27017

mongo> sh.addShard("localhost:27020")
mongo> sh.addShard("localhost:27021")
mongo> sh.addShard("localhost:27022")
mongo> sh.addShard("localhost:27023")
mongo> sh.addShard("localhost:27024")
mongo> sh.addShard("localhost:27025")
mongo> sh.addShard("localhost:27026")
mongo> sh.addShard("localhost:27027")
mongo> sh.enableSharding("wiki")
mongo> sh.shardCollection("wiki.articles", { "\_id": "hashed" })
'''

## Loading the data

Download the wikipedia dataset and parse it using the conversion 
[tools](../benchmark/datasets/wikiparse/).
