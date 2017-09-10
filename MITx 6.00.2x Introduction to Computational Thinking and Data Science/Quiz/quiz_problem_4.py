# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:36:44 2017

@author: szahn
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    
    working_s = s
    m = []
    
    for i in range(len(L)):
        res = working_s // L[i]
        m.append(res)
        working_s -= ( res * L[i])
        
    if sum([i*j for i, j in zip(L, m)]) == s:
        return sum(m)
    else:
        return 'no solution'
    
    
 
    
    
    
    
    
    
    
# this was my original submission, I tried cleaning it up afterwards
def greedySum_2(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    
    len_L = len(L)
    working_s = s
    m = []
    
    for i in range(len_L):
        res = working_s // L[i]
        m.append(res)
        working_s -= ( res * L[i])
    
    sum_m = sum(m)
    
    lm_sum = 0
    for i, j in zip(L, m):
        lm_sum += i*j
    
    if lm_sum == s:
        return sum_m
    else:
        return 'no solution'