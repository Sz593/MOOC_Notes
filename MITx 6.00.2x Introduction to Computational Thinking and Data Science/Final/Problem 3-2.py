# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:42:22 2017

@author: szahn
"""

import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    results_true_count = 0
    for i in range(numTrials):
        balls = ['g1', 'g2', 'g3', 'g4', 'r1', 'r2', 'r3', 'r4']
        picked = []
        for j in range(3):
            picked_ball = random.choice(balls)
            picked.append(picked_ball)
            balls.remove(picked_ball)
        if picked[0][0] == picked[1][0] == picked[2][0]:
            results_true_count += 1
    
    return results_true_count / numTrials