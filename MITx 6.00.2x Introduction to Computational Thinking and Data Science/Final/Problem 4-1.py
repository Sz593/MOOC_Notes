# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:47:42 2017

@author: szahn
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title is not None:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    list_of_runs = []
    
    for trial in range(numTrials):
        rolls = []
        trial_run_counter = []
        
        for i in range(numRolls):
            roll = die.roll()
            rolls.append(roll)
            
            if i == 0:
                trial_run_counter.append(1)
            else:
                if rolls[i] == rolls[i - 1]:
                    trial_run_counter.append(trial_run_counter[i - 1] + 1)
                else:
                    trial_run_counter.append(1)

        list_of_runs.append(max(trial_run_counter))
    
    makeHistogram(list_of_runs, 10, 'Longest Run', 'Number of Occurrences')
    final_mean, final_std = getMeanAndStd(list_of_runs)
    
    return final_mean
    
    
            
    
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))