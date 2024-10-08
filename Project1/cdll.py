class MyNode:
    def __init__(self, _data):
        self.data = _data
        self.next = None
        self.prev = None

class MyList:
    def __init__(self, _data):
        self.head = MyNode(_data)
        self.head.prev = self.head
        self.head.next = self.head
        self.tail = self.head

        if _data is None:
            self.length = 0
        else:
            self.length = 1

    def forwardSearch(self, _data):
        currentNode = self.head
        count = 0
        while count < self.length:
            if currentNode.data == _data:
                return currentNode
            currentNode = currentNode.next
            count += 1
        return None

    def append(self, _data):
        if self.head == None:
            self.head = MyNode(_data)
            self.head.prev = self.head
            self.head.next = self.head
            self.tail = self.head
            return
        else:
            self.tail.next = MyNode(_data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1

    def remove(self, _data):
        currentNode = self.forwardSearch(_data)
        if currentNode is None: # data searched for not found
            print(f'{_data} not found, remove operation failed.')
            return
        else:
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            if currentNode is self.head:
                self.head = currentNode.next
            elif currentNode is self.tail:
                self.tail = currentNode.prev
            del currentNode
        self.length -= 1

    def dis(self): # display
        if self.head is None:
            print('CDLL[]')
            return
        node = self.head
        print('CDLL[' + str(node.data), end='')
        if node.next is self.head:
            print(']')
        count = 0
        while count < self.length-1:
            node = node.next
            if node.next is not self.head:
                print(f', {str(node.data)}', end='')
            else:
                print(f', {str(node.data)}', end=']\n')
            count += 1