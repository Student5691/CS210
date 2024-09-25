x = [13,86,35,1,100,45,11,6,67,65,2,7,23,23,23,87,38,67,31,99,1,1,100]
y = [13,86,35,1,100,45,11,6,67,65,2,7,23,23,23,87,38,67,31,99,1,1,100]

def shellSort(arr):
    gap = len(arr)//2
    while gap > 0:
        for i in range(0, len(arr)-gap, 1):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                for j in range(i, gap-1, -gap):
                    if arr[j] < arr[j-gap]:
                        arr[j], arr[j-gap] = arr[j-gap], arr[j]
                    else:
                        break
        gap = gap//2

print("unsorted:\t", x)
shellSort(x)
print("shellSort:\t", x)
print("Python sort:\t",sorted(y))