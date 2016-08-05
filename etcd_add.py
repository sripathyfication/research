#!/usr/bin/env python
import os
import sys

tenant_start = 1000
bd_start = 2000
mac_start = 0x0a0b0c00001
port = 1

for t in range(0,10):
	key_t = "etcdctl mk /" + str(t + tenant_start)
	for b in range(0,10):
		key_b = key_t + "/" + str(bd_start + b)
		for m in range(0,10):
			key_m = key_b + "/" + str(mac_start + m) + " \"Eth1/1\""
			os.system(key_m)
	key_t = ""
		
