class MyNode:
    def __init__(self, _data):
        self.data = _data
        self.next = None

class MyLinkedList:
    def __init__(self, _data):
        self.head = MyNode(_data)

    def getLastElement(self, node):
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    def append(self, _data):
        if self.head == None:
            self.head = MyNode(_data)
            return
        else:
            lastNode = self.getLastElement(self.head)
            lastNode.next = MyNode(_data)

    def display(self):
        if self.head is None:
            print('LL[]')
            return
        node = self.head
        print('LL[' + str(node.data), end='')
        if node.next is None:
            print(']')
        while node.next is not None:
            node = node.next
            if node.next is None:
                print(f', {str(node.data)}', end=']\n')
            else:
                print(f', {str(node.data)}', end='')


    def remove(self, _data):
        current, prev = self.head, None
        while current is not None:
            if current.data == _data:
                prev.next = current.next
                del current
                return self.head
            current, prev = current.next, current

x = MyLinkedList(5)
x.display()
x.append(8)
x.display()
x.append(322)
x.display()
x.append(455)
x.display()
x.remove(455)
x.display()
x.remove(432432)
x.display()