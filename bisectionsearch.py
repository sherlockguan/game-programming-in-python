#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:09:02 2020

@author: guanfang
"""
#
#def bisect_search1(L,e):# list copy and recursion increase time and space complexity
#    if L == []:
#        return False
#    elif len(L) == 1:
#        return L[0] == e
#    else:
#        half = len(L) // 2
#        if L[half] > e:
#            return bisect_search1(L[:half],e)#copy half of the list and recursion
#        else:
#            return bisect_search1(L[half:],e)
#        
        
        
def bisect_search2(L,e):
    def bisect_search_helper(L,e,low,high):
        if high == low:
            return L[low] == e #return if this boolean value is true
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False #one element
            else:
                return bisect_search_helper(L,e,low,mid-1)
        else:
            return bisect_search_helper(L,e,mid+1,high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L,e,0,len(L)-1)
        
testList = [1,2,3,5,7,9,18,27]