class MyList:
    '''
    Custom list class that handles input of a single list or a sequence of other data types.
    Includes methods for appending and removing data, as well as a length member that maintains the list length as an integer.
    Includes the __str__ method, returning the contents of the array member for use with Python's print() function.
    '''
    def __init__(self, *args):
        if  isinstance(args[0], list):
            self.array = args[0]
            index = 0
            while True:
                try:
                    i = self.array[index]
                    index += 1
                except IndexError:
                    break
                except:
                    print('Error in __init__ method while counting length of input array')
                    break
        else:
            self.array = []
            index = 0
            while True:
                try:
                    self.array += [args[index]]
                    index += 1
                except IndexError:
                    break
                except:
                    print('Error in __init__ method while assigning multiple args to the MyList object instance')
                    break
        self.length = index

    def my_append(self, val):
        self.array += [val]
        self.length += 1

    def my_remove_slicing(self, val):
        i = 0
        while i <= self.length-1:
            if self.array[i] == val:
                self.array = self.array[:i] + self.array[i+1:]
                self.length -=1
                return
            i += 1
    
    def my_remove_tempArray(self, val):
        i = 0
        temp_arr = []
        vals_removed = 0
        while i < self.length:
            if self.array[i] == val and vals_removed == 0:
                i += 1
                vals_removed = 1
            else:
                temp_arr += [self.array[i]]
                i += 1
        self.array = temp_arr
        self.length -= 1
        temp_arr = []

    def __str__(self):
        return f"[{', '.join(map(str, self.array))}]"

arr = [1,3,5,6,8,9,12,13,None,15,17,18,24,True,36,47,58,3,98,'432',4,3,42,'fdsa']
z = MyList(arr)

print(f'{'Starting array, "arr":':<35} {arr}')
print(f'{'MyList using "arr":':<35} {z}')

remove = 1
z.my_remove(remove)
print(f'{'Removing ' + str(remove) + ':':<35} {z}')

remove = 24
z.my_remove(remove)
print(f'{'Removing ' + str(remove) + ':':<35} {z}')

remove = 'fdsa'
z.my_remove(remove)
print(f'{'Removing ' + str(remove) + ':':<35} {z}')

apnd = 1111
z.my_append(apnd)
print(f'{'Appending ' + str(apnd) + ':':<35} {z}')

print(f'{'Final list:':<35} {z}')