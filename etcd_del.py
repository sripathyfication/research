#!/usr/bin/env python
import os
import sys

os.system("etcdctl ls --recursive > keys")
key_f = open("keys","r")
for line in key_f:
	cmd_s = "etcdctl rm --dir " + line
	print cmd_s
	os.system(cmd_s)		
