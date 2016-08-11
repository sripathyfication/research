#!/usr/bin/env python
# 
# etcdctl helper written in python.
# --
# makes use of simplejson, pycurl to fetch keys,stats from etcd leader 
# and writes to a file or prints it pretty.
#
# TODO: 1. add support for all etcdctl commands.
#       2. take input from user to either write to a file
#       or print it.
#       3. Extend it to take input for leader ip, all servers in cluster etc.
#
# Author: Sripathy Ramaswamy. 
# Date: 8/11/2016, San Jose, CA
#
#
#-----------------------------------------------------------------------------------
import sys
import os
import requests
import time
import simplejson as json
import pycurl
from StringIO import StringIO

etcd_leader_="http://172.29.202.33:2379"

def get_keys():
    cmd = etcd_leader_ + "/v2/keys"
    print "\n..getting keys via curl -L " + cmd + " .. and writing to keys.json\n"
    with open('keys.json','wb') as f:
        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL,cmd)
        c.setopt(c.WRITEDATA,buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        obj = json.loads(body)
        f.write (json.dumps(obj, separators=(',',':'),sort_keys=True, indent=4 * ' '))

def get_stats():
    cmd = etcd_leader_ + "/v2/stats/store"
    print "\n..getting stats via curl -L " + cmd + "\n"
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL,cmd)
    c.setopt(c.WRITEDATA,buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    obj = json.loads(body)
    print (json.dumps(obj, separators=(',',':'),sort_keys=True, indent=4 * ' '))


def display_options():
	print "Python ETCD CTL Helper"
	print "----------------------"
	print "get -- Get all keys from leader"
	print "stats -- Get store stats from leader"
	print "help -- Display this help"

options = {
		  'get': get_keys,
		  'stats': get_stats,
		  }

def validate(op):
    if op in options:
        return True
    else:
        return False

def main():
    while True:
        display_options()
        op = raw_input("Enter your option\n")
        if validate(op):
           break
    options[op]()
	
	
if __name__=='__main__':
	main()
