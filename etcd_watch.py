#!/usr/bin/env python
import os
import sys

key = "/1000/2001/"

cmd_s = "etcdctl exec-watch --recursive " + key +  " -- sh -c \"env | grep ETCD_WATCH >> modified.keys\""

os.system(cmd_s)
