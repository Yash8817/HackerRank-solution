#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(my_val):
    
    pos_val = 0
    neg_val = 0
    zero_val = 0
    for i in my_val:
        if i == 0 :
            zero_val += 1

        elif i < 0:
            neg_val += 1
        elif i > 0:
            pos_val += 1
    total = len(my_val)
    pos_res = pos_val / total
    neg_res = neg_val / total
    zero_res = zero_val / total
    
    print("{:.6f}".format(pos_res))
    print("{:.6f}".format(neg_res))
    print("{:.6f}".format(zero_res))
            
            
        
    
total_val = int(input())

my_val= list(map(int,input().split())) 

plusMinus(my_val)
