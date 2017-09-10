# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:46:30 2017

@author: szahn
"""

import random

class Bucket():
    def __init__(self):
        self.red_balls = 3
        self.green_balls = 3
        
    def get_contents(self):
        print(f'There are {self.red_balls} red balls and {self.green_balls} green balls.')
    
    def remove_ball(self, color):
        if color.lower() == 'g' or color.lower() == 'green':
            self.green_balls -= 1
        elif color.lower() == 'r' or color.lower() == 'red':
            self.red_balls -= 1
        else:
            raise ValueError('Please enter a valid ball color: red or green.')
    
    def all_one_color_left(self):
        if self.red_balls == 3 and self.green_balls == 0:
            return True
        elif self.red_balls == 0 and self.green_balls == 3:
            return True
        else:
            return False



def noReplacementSimulation(numTrials):
    num_success = 0
    for i in range(numTrials):
        b = Bucket()
        list_of_balls = ['g1', 'g2', 'g3', 'r1', 'r2', 'r3']
        for j in range(3):
            ball_choice = random.choice(list_of_balls)
            list_of_balls.remove(ball_choice)
            b.remove_ball(ball_choice[0])
        if b.all_one_color_left() == True:
            num_success += 1
    return num_success / numTrials