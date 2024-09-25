x = [13,86,35,1,100,45,11,6,67,65,2,7,23,23,23,87,38,67,31,99,1,1,100]
y = [13,86,35,1,100,45,11,6,67,65,2,7,23,23,23,87,38,67,31,99,1,1,100]

def quickSort(arr):
    if len(arr) <= 0:
        return arr
    
    pivot_i = len(arr)//2
    pivot = arr[pivot_i]
    left, mid, right = [], [], []

    for i in arr:
        if i < pivot:
            left += [i]

    for j in arr:
        if j == pivot:
            mid += [j]

    for k in arr:
        if k > pivot:
            right += [k]
    
    return quickSort(left) + mid + quickSort(right)

print("unsorted:\t", x)
print("quickSort:\t", quickSort(x))
print("Python sort:\t",sorted(y))