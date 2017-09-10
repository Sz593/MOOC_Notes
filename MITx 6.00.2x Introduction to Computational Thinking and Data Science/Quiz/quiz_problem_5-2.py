# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:59:18 2017

@author: szahn
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    max_sum = 0
#    max_contig_seq = []
    L_len = len(L)
    
    for i in range(L_len + 1):
#        print('Checking all sequences of length {}.'.format(i))
        
        for j in range(L_len):
            contig_seq = L[j:i]
            sum_contig_seq = sum(contig_seq)
            
            if sum_contig_seq > max_sum:
#                max_contig_seq = contig_seq
                max_sum = sum_contig_seq
                
    return max_sum