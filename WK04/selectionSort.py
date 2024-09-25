x = [13,86,35,1,100,45,11,6,67,65,2,7,23,23,23,87,38,67,31,99,1,1,100]
y = [13,86,35,1,100,45,11,6,67,65,2,7,23,23,23,87,38,67,31,99,1,1,100]

def selectionSort(arr):
    for i in range(0, len(arr)-1, 1):
        for j in range(i+1, len(arr)-1, 1):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

def revSelectionSort(arr):
    for i in range(0, len(arr)-1, 1):
        for j in range(i+1, len(arr)-1, 1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

print("unsorted:\t", x)
selectionSort(x)
print("selectionSort:\t", x)
print("Python sort:\t", sorted(y))