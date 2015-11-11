'''
An exercise to practice collaboration using git and Github.
Author: Bosco Noronha (nbosco)
Date: 25th Oct 2015
'''

import random

'''
Purpose of the function:
Given a array of integers, return the length of the array.
Eg. Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output: 8
'''
def amountInArray(array):
    return len(array)


'''
Purpose of the function:
Given a array of integers, return the sum of all the integers.
Eg. Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output:
'''
def sumOfArray(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

'''
Purpose of the function:
Given a array of integers, return the array in reverse order.
Eg. Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output:[8, 7, 6, 5, 4, 3, 2, 1]
'''
def reverseArray(array):
    reverse = []
    for i in range(len(array)):
        reverse.append[array[len(array)-1]]
    return reverse


'''
Purpose of the function:
Given a array of integers, return the array shuffled.
Eg. Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output:[8, 2, 1, 5, 7, 3, 4, 6]
'''
def shuffleArray(array):
    rand = random.shuffle(array)
    return rand



#MAIN
array = [1, 2, 3, 4, 5, 6, 7, 8]

print amountInArray(array)
print sumOfArray(array)
print reverseArray(array)
print shuffleArray(array)
