#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:13:37 2020

@author: guanfang
"""
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal
caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]

def pleaseConform(caps):
    #Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []
    # A dummy(false, defaut)end
    caps = caps + ['END']
    #print(caps)
    #determine intervals where caps are on in the same direction
    for i in range(1,len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start,i-1,caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
## # NO Need to to add the last interval after loop completes execution
##    intervals.append((start,len(caps)-1,caps[start]))
#    if caps[start] == 'F':
#        forward += 1
#    else:
#        backward += 1
    #print(caps)
    #print(intervals)
    #print(forward,backward)

# minimum num of caps-flip
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals: # every turple in interval has 3 element (start end dir)
        if t[2] == flip:
            if t[0]!= t[1]:
                print('people in position',t[0],'through',t[1],'flip your hats')
            else: # case when only one element in this interval
                print('people in position',t[0],'flip your cap')
            
    


pleaseConform(caps)
print('')
pleaseConform(cap2)
