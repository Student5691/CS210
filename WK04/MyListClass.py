class MyList:
    '''
    custom list class that handles input of a single list or a sequence of other data types.
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
        self.length = index

    def my_append(self, val):
        self.array += [val]
        self.length += 1

    def my_remove(self, val):
        i = 0
        while i <= self.length-1:
            if self.array[i] == val and i > self.length//2:
                j = i
                while j < self.length-1:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    j += 1
                self.array = self.array[:-1]
                self.length -=1
                return
            elif self.array[i] == val and i <= self.length//2:
                j = i
                while j > 0:
                    self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
                    j -= 1
                self.array = self.array[1:]
                self.length -=1
                return
            i += 1

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