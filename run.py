#! /usr/bin/python3

import time
import os
import psutil
if os.path.isfile(".twitter_stream_data.txt"):
    os.remove(".twitter_stream_data.txt")

topic = input("Search : ")
process=os.popen("python3 twitter_live_analysis.py "+topic)
time.sleep(10)
proc=0
for process in psutil.process_iter(attrs=['pid','name']):
    if 'python' in process.info['name']:
        proc=process.info['pid']

os.system("python3 twitter_graph.py")
time.sleep(3)
os.system("kill -9 "+str(proc))
del process
