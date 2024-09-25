class MyList:
    '''
    custom list class that handles input of a single list or a sequence of other data types.
    '''
    def __init__(self, *args):
        if  isinstance(args[0], list):
            self.array = args[0]
        else:
            self.array = []
            while args != None:
                self.array +=[args]
            # for arg in args:
            #     self.array += [arg]
        
    def my_len(self):
        length = 0
        while True:
            try:
                i = self.array[length]
                length += 1
            except:
                break
        # for i in self.array:
        #     length += 1
        return length

    def my_append(self, val):
        self.array += [val]
        return self.array

    def my_remove(self, val):
        for i in range(self.my_len()-1):
            if self.array[i] == val:
                if i > self.my_len()//2:
                    for j in range(i, self.my_len()-1, 1):
                        self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.array = self.array[:-1]
                else:
                    for j in range(i, 0, -1):
                        self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
                    self.array = self.array[1:]
                return self.array
    
    def __str__(self):
        return f"[{', '.join(map(str, self.array))}]"

arr = [1,3,5,6,8,9,12,13,None,15,17,18,24,True,36,47,58,3,98,'432',4,3,42,'fdsa']

z = MyList(arr)
print('Starting array, "arr":\t', arr)
print('MyList using "arr":\t', z)
remove = 24
print(f'Removing "{remove}":\t\t', z.my_remove(remove))
apnd = 1111
print(f'Appending "{apnd}":\t', z.my_append(apnd))
print('Final list:\t\t',z)