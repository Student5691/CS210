x = [13,86,35,1,100,45,11,6,67,65,2,7,23,23,23,87,38,67,31,99,1,1,100]
y = [13,86,35,1,100,45,11,6,67,65,2,7,23,23,23,87,38,67,31,99,1,1,100]

def insertionSort(arr):
    for i in range(1, len(arr), 1):
        val = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > val:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break

print("unsorted:\t", x)
insertionSort(x)
print("insertionSort:\t", x)
print("Python sort:\t", sorted(y))