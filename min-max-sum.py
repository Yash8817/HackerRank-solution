#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(my_list):

    sum0 = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    for i in range(0,len(my_list)):
        if i == 0 :
            sum0 = my_list[1] +my_list[2]+my_list[3]+my_list[4]
        elif i == 1:
            sum1 = my_list[0] +my_list[2]+my_list[3]+my_list[4]
        elif i == 2:
            sum2 = my_list[0] +my_list[1]+my_list[3]+my_list[4]
        elif i == 3:
            sum3 = my_list[0] +my_list[1]+my_list[2]+my_list[4]
        elif i == 4:
            sum4 = my_list[0] +my_list[1]+my_list[2]+my_list[3]

    my_sum = [sum0,sum1,sum2,sum3,sum4]
    min_sum = min(my_sum)
    max_sum = max(my_sum)
    print(min_sum, end = ' ')
    print( max_sum)

my_list = list(map(int,input().split())) 

miniMaxSum(my_list)

