
import datetime as dt

dt.datetime.now()

import random as rd

rd.choice(["blue","green","yellow"])
rd.randint(-1,150)
rd.seed(1234)
rd.randint(0,1)

import numpy as np

beta = np.random.randint(10,100,1000)

print(beta)

def sticazzi(arg1,arg2):
    """ this is a test help for function sticazzi \n
    it takes two variables \n
    arg1 amd arg2"""
    print(arg1+arg2)

argomento1 ="e allora"
argomento2  = "mortacci"
sticazzi(arg1=argomento1,arg2=argomento2)

sticazzi(argomento2,argomento1)