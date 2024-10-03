class MyNode:
    def __init__(self, _data):
        self.data = _data
        self.next = None
        self.prev = None

class MyDoublyLinkedList:
    def __init__(self, _data):
        self.head = MyNode(_data)
        self.tail = self.head
        if _data is None:
            self.length = 0
        else:
            self.length = 1

    def append(self, _data):
        if self.head == None:
            self.head = MyNode(_data)
            self.tail = self.head
            return
        else:
            self.tail.next = MyNode(_data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.length += 1

    def dis(self): # display
        if self.head is None:
            print('DLL[]')
            return
        node = self.head
        print('DLL[' + str(node.data), end='')
        if node.next is None:
            print(']')
        while node.next is not None:
            node = node.next
            if node.next is None:
                print(f', {str(node.data)}', end=']\n')
            else:
                print(f', {str(node.data)}', end='')

    def forwardSearch(self, _data):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == _data:
                return currentNode
            currentNode = currentNode.next
        return None

    def remove(self, _data):
        currentNode = self.forwardSearch(_data)
        if currentNode is None: # data searched for not found
            print(f'{_data} not found, remove operation failed.')
            return
        elif currentNode.next is None: # handles edge case: tail
            currentNode.prev.next = None
            self.tail = currentNode.prev
            del currentNode
            
        elif currentNode.prev is None: # handles edge case: head
            currentNode.next.prev = None
            self.head = currentNode.next
            del currentNode
            
        else: # handles removal of any other position within the linked list
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            del currentNode
        self.length -= 1

x = MyDoublyLinkedList(0)

for i in range(1, 10, 1):
    x.append(i)

print('Initial Doubly Linked List')
x.dis()
print(f'Head: {x.head.data} \tTail: {x.tail.data}  \tLen: {x.length}\n')

x.remove(0)
print('Edge case: head - Remove 0')
x.dis()
print(f'Head: {x.head.data} \tTail: {x.tail.data}  \tLen: {x.length}\n')

x.remove(9)
print('Edge case: tail - Remove 9')
x.dis()
print(f'Head: {x.head.data} \tTail: {x.tail.data}  \tLen: {x.length}\n')

x.remove(5)
print('Middle case - Remove 5')
x.dis()
print(f'Head: {x.head.data} \tTail: {x.tail.data}  \tLen: {x.length}\n')

print('Data-not-found case - Remove 20')
x.remove(20)
x.dis()
print(f'Head: {x.head.data} \tTail: {x.tail.data}  \tLen: {x.length}\n')

print('Append 21')
x.append(21)
x.dis()
print(f'Head: {x.head.data} \tTail: {x.tail.data}  \tLen: {x.length}\n')