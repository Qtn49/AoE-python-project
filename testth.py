#!/usr/bin/env python3
# coding: utf-8
import threading
import time

class SUP(threading.Thread):

    def run(self,t):
        for i in range(1, 11):
            time.sleep(1)
            print(i)
        print(t)

ob = SUP()
threading.Thread(target=ob.run, args=("r",)).start()
assert False,"pute"
