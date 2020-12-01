""" Functions for permutations """

from itertools import combinations
from numpy import prod, unique

def multiplicativeSum(listOfNumbers,sumGoal,numberOfItems):
    """ Return the product for the numberOfItems in the listOfNumbers when the sum of the items
        is equal to sumGoal.
        multiplicativeSum([1,2,3],5,2) = 6 """
    allCombinations = combinations(listOfNumbers,numberOfItems)
    return [prod(item) for item in allCombinations if sum(item)==sumGoal][0]