x = [100,65,11,7,8,8,8,5,3,18,3,5,1,2,34,76,3,3,98]
y = sorted(x)
z = list(reversed(y))

# class example
# def isSorted(arr):
#     return arr == sorted(arr) or arr == list(reversed(sorted(arr)))

def isSorted(arr: list) -> tuple | bool:
    '''
    isSorted checks to see if the input list/array is in ascending or descending order.

    Parameters
    ----------
    arr : list
        Input array of values

    Returns
    -------
    tuple | bool
        If the input list/array is sorted, returns a tuple with two entries: boolean True and either "ascending" or "descending".\n
        Otherwise returns the boolean, False.
    '''
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            for j in range(len(arr)-2):
                if arr[j+1] < arr[j+2]:
                    return False
                else:
                    continue
            return True, 'descending'
        else:
            continue
    return True, 'ascending'


def bubble_sort(arr: list, ascending: bool = True) -> list:
    '''
    bubble_sort takes in a list/array and, based on the optional bool parameter,\n
    sorts the array in ascending (default) or descending order.

    Parameters
    ----------
    arr : list
        Input array of values
    ascending : bool, optional
        Sort the list in ascending (True) or descending (False) order, by default True

    Returns
    -------
    list
        Returns a sorted list/array with respect to the input list/array
    '''

    if ascending == False:
        for j in range(len(arr)):
            for i in range(len(arr)-1, 0+j, -1):
                if arr[i] > arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
    else:
        for j in range(len(arr)):
            for i in range(len(arr)-1-j):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print('\nTesting "isSorted" Function\n')

print('x is not sorted.\t\t\tTesting: is x sorted?', isSorted(x))
print('y is sorted in ascending order.\t\tTesting: is y sorted?', isSorted(y))
print('z is sorted in descending order.\tTesting: is z sorted?', isSorted(z))

print("\n------------------------------------------------------\n")

print('Testing "bubble_sort" Function\n')

print("Unsorted starting array:\n", x)
print("\nAfter bubble_sort, ascending:\n", bubble_sort(x, True))
print("Compared to Python sorting:\n", y)

print("\nAfter bubble_sort, descending:\n", bubble_sort(x, False))
print("Compared to Python reversed array:\n", z)
print()