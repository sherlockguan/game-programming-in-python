#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:29:37 2020

@author: guanfang
"""
#mergeSort: Recursive Divide-and-Conquer algorithm.
def mergeSort(L):
    
    if len(L) == 2:
        if L[0]<= L[1]:
            return [L[0],L[1]]
        else:
            return [L[1],L[0]]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left,right)
    
    
    
def merge(left,right):
    
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while(i < len(left)):
        result.append(left[i])
        i+=1
    while(j<len(right)):
        result.append(right[j])
        j+=1
    return result
inp = [23, 3, 45, 7, 6, 11, 14, 12]
