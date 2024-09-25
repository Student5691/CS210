def twoNumSum(nums, target):
    hashTable = {}
    for i in range(len(nums)):
        if target - nums[i] in hashTable:
            return [hashTable[target - nums[i]], i]
        hashTable[nums[i]] = i
    return [-1, -1]

a = [2,7,11,15]
target = 9

[firstIndex, secondIndex] = twoNumSum(a,target)

if firstIndex != -1:
    print(f'''\nThe value at index {firstIndex} is {a[firstIndex]}. The value at index {secondIndex} is {a[secondIndex]}.''')
    print(f'Added together, they are {a[firstIndex]+a[secondIndex]}, which should be equal to the target, {target}.\n')
else:
    print(f'\nNo two numbers in this array add up to the target, {target}.\n')