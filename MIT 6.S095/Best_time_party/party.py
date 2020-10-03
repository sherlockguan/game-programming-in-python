#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:48:23 2020

@author: guanfang
"""
# global variable
sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
         (9, 10), (10, 11), (10, 12), (11, 12)]

def bestTimeToParty(schedule): #Wrapper function
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:
        start = min(start,c[0])
        end = max(start, c[1])
    
    count = count_celebrity(schedule,start, end)
    max_count = 0
    for i in range(len(count)):
        if count[i] > max_count:
            max_count = count[i]
            time = i
        
   
    
    
    print('best time to attend a party is',time," o'clock",max_count,
    'celebrities will be attending')
    

# # for each time, count arrivals and record the responding time i as time_variable
def count_celebrity(schedule,start,end): # write THIS FUNC FIRST
    count = [0]*(end + 1)  # 13 is "magic number" fewer code but few variable may cause ambiguousity
    
    for i in range(start, end + 1):
        count[i] = 0
        for c in schedule:
            if c[0] <= i and c[1]> i:
                count[i]+= 1

    return count # test it seperately
    #count_celebrity(sched)

    #[0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 4, 4, 0]

bestTimeToParty(sched)






    
    
        
