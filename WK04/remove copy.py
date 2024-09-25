class MyList:
    '''
    list class created from scratch that handles int, float, and list only
    '''
    def __init__(self, *args):
        if  isinstance(args[0], list):
            self.array = args[0]
        else:
            self.array = []
            for arg in args:
                self.array += [arg]
        print(self.array)
        # else:
        #     raise TypeError("TypeError: MyList expected at most one array as the argument.")
        # if userInput == None:
        #     self.array = []
        # elif isinstance(userInput, int) or isinstance(userInput, float):
        #     self.array = [userInput]


    # def my_append(self, val):
    #     return self.array + MyList(val)
        
        
        
        
    def my_remove():
        return


arr = [1,3,5,6,8,9,12,13,15,17,18,24,36,47,58,98]

# z = MyList(1,5,3,9,'a','f','g')
z = MyList(arr)

print(type(z))
print(z)


# for item in z:
#     print(item)
# z.my_append(111111)
# print(z)

# remove = 13

# for i in range(len(arr)):
#     if arr[i] == remove:
#         removeIndex = i
#         for j in range(i, len(arr)-1):
#             arr[j] = arr[j+1]


# print(arr)