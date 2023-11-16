import random
import sys
from disk_struct import Disk
from page_replacement_algorithm import  page_replacement_algorithm
from CacheLinkedList import  CacheLinkedList
import numpy as np

import PyIO
import PyPluMA

import ALeCaR0
import ALeCaR1
import ALeCaR2
import ALeCaR3
import ALeCaR4_adaptive
import ALeCaR4
import ALeCaR5_adaptive2
import ALeCaR5_adaptive
import ALeCaR5_freqdist
import ALeCaR5
import ALeCaR6_adaptive
import ALeCaR6
import ALeCaR7
import ALeCaR8


class ALeCaRPlugin:
  def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)

  def run(self):
        pass

  def output(self, outputfile):
    n = int(self.parameters["n"])
    infile = open(PyPluMA.prefix()+"/"+self.parameters["infile"], 'r')
    kind = self.parameters["kind"]
    outfile = open(outputfile, 'w')
    outfile.write("cache size "+str(n))
    if (kind == "ALeCaR0"):
       alecar = ALeCaR0.ALeCaR0(n)
    elif (kind == "ALeCaR1"):
       alecar = ALeCaR1.ALeCaR1(n)
    elif (kind == "ALeCaR2"):
       alecar = ALeCaR2.ALeCaR2(n)
    elif (kind == "ALeCaR3"):
       alecar = ALeCaR3.ALeCaR3(n)
    elif (kind == "ALeCaR4_adaptive"):
       alecar = ALeCaR4_adaptive.ALeCaR4(n)
    elif (kind == "ALeCaR4"):
       alecar = ALeCaR4.ALeCaR4(n)
    elif (kind == "ALeCaR5_adaptive2"):
       alecar = ALeCaR5_adaptive2.ALeCaR5(n)
    elif (kind == "ALeCaR5_adaptive"):
       alecar = ALeCaR5_adaptive.ALeCaR5(n)
    elif (kind == "ALeCaR5_freqdist"):
       alecar = ALeCaR5_freqdist.ALeCaR5(n)
    elif (kind == "ALeCaR5"):
       alecar = ALeCaR5.ALeCaR5(n)
    elif (kind == "ALeCaR6_adaptive"):
       alecar = ALeCaR6_adaptive.ALeCaR6(n)
    elif (kind == "ALeCaR6"):
       alecar = ALeCaR6.ALeCaR6(n)
    elif (kind == "ALeCaR7"):
       alecar = ALeCaR7.ALeCaR7(n)
    else:
       alecar = ALeCaR8.ALeCaR8(n)
    page_fault_count = 0
    page_count = 0
    for line in infile:
        line = int(line.strip())
        outfile.write("request: "+str(line))
        if alecar.request(line) :
            page_fault_count += 1
        page_count += 1

    
    outfile.write("page count = "+str(page_count))
    outfile.write("\n")
    outfile.write("page faults = "+str(page_fault_count))
    outfile.write("\n")
