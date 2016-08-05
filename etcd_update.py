#!/usr/bin/env python
import os
import sys

cmd_ = "etcdctl ls --recursive " + sys.argv[1]
os.system(cmd_ + " > update.keys")
key_ = open("update.keys","r")

for line in key_:
	cmd_ = line[:len(line) -1]
	cmd_ = "etcdctl update " + cmd_ +  " Eth1/1"
	print cmd_
	os.system(cmd_)
