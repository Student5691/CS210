# Python Version 3.12

# Problem 1.
# Linear search is a search algorithm that starts from the beginning of an array,
# and checks each element until the search key is found or the end of the array is reached.
print('\nProblem 1:')
x = [15, 4, 18, 8, 19, 22, 24, 59, 59, 20, 18, 12, 36, 42, 9] # Given array
target1 = 24 # Given target to find within the array, x

for i in range(len(x)): # for loop cycling from each index of the array, x
    if x[i] == target1: #check to see if the element at index "i" or array "x" is equal to the value in the target1 variable
        # if true
        print('Target: ', target1, ' found at index: ', i, '.', sep='')
        # print the above statement to the console
        break # breaks from the for loop

# Question: Is there a more efficient way to do it?
# Only if the array is sorted, then we could use a binary search instead of a linear search.
# A binary search would give a time complexity of O(log n) instead of O(n)


# Problem 2.
# Given an array of integers "nums" and an integer "target",
# return indices of the two numbers such that they add up to target

print('\nProblem 2:')
nums = [1,2,4,76,34,16,94,56,34,12,97,54,32,22,85,67,56,98,99,100] # Arbitrarily selected array
target = 199 # Chosen value to be the solution when adding two elements of the array, nums, together
done = False # flag variable to allow breaking from the external for loop upon discovering the solution; assumes only one solution

for i in range(len(nums)-1): # outer for loop ascending through all but the last index values of the array, nums; last index value excluded as there are no more values in "nums" to add with
    for j in range(i+1, len(nums)): # j starts from index position i+1 to ensure we don't add nums[1] itself, nums[17] to itself, etc. per problem directions
        if nums[i] + nums[j] == target: # check to see if the sum of nums[i] and nums[j] are equal to the value in the target variable
            # if true
            index_i = i # store the solution indices for future use per problem direction "return indices of the two numbers..."
            index_j = j
            print(nums[index_i], ' at index ', index_i, ' added to ', nums[index_j], ' at index ', index_j, ' equals the target: ', target, '.\n', sep='')
            # print the above statement to the console
            done = True # change the "done" variable to "True"
            break # breaks from the inner for loop
    if done == True:
        # once a solution is found, "done" is set to "True" and then this if statement will evaluate as true
        break # breaks from the outer for loop when "done" = "True"