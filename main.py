import random
import sys
from disk_struct import Disk
from page_replacement_algorithm import  page_replacement_algorithm
from CacheLinkedList import  CacheLinkedList
import numpy as np

# sys.path.append(os.path.abspath("/home/giuseppe/))

if __name__ == "__main__" :
    if len(sys.argv) < 2 :
        print("Error: Must supply cache size.")
        print("usage: python3 [cache_size]")
        exit(1)

    n = int(sys.argv[1])
    infile = open(sys.argv[2], 'r')
    print("cache size ", n)

    lru = LRU(n)
    page_fault_count = 0
    page_count = 0
    for line in infile:
        print("request: ", line)
        if lru.request(line) :
            page_fault_count += 1
        page_count += 1


    print("page count = ", page_count)
    print("page faults = ", page_fault_count)
