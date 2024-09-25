# Python 3.12

import random

def bin_search(nums, target):
    lowIndex = 0
    highIndex = len(nums)-1
    count = 0

    while lowIndex <= highIndex:
        count += 1
        guess = (lowIndex + highIndex)//2
        if nums[guess] == target:
            return guess, count
        elif nums[guess] < target:
            lowIndex = guess + 1
        else:
            highIndex = guess - 1
    return -1, count

a=[1]
for i in range(2000):
    if random.randint(0,10) == 5:
        a.append(1000+i)
    if len(a) == 99:
        break
a.append(10000)
print(a)

target = a[random.randint(0,len(a)-1)]
if random.randint(0,1) == 1:
    target = 0

solution, iterations = bin_search(a,target)

if solution != -1:
    print('\nTarget:', target, 'found at index:', solution, '( check:', a[solution], ') after', iterations, 'guesses.\n')
else:
    print('\nTarget:', target, 'not found in the array after', iterations, 'guesses.\n')