class Node:
    def __init__(self, _data):
        self.data = _data
        self.next = None

class MyLinkedList:
    def __init__(self, _data):
        self.head = Node(_data)
        self.tail = None
        
    def getLastNode(self, lastNode):
        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        return lastNode

    def my_append(self, _data):
        if self.head == None:
            self.head = Node(_data)
            return
        self.getLastNode(self.head).next = Node(_data)

    def my_remove(self, _data):
        current, prev = self.head, None
        while current is not None:
            if current.data == _data:
                prev.next = current.next
                del current
                print(f'"{_data}" removed.')
                return
            current, prev = current.next, current
        print(f'"{_data}" not found; remove operation failed.')
            
    def my_search(self, _data):
        current = self.head
        while current is not None:
            if current.data == _data:
                print(f'"{_data}" found.')
                return current
            current = current.next
        print(f'"{_data}" not found')
        return Node(f'"{_data}" not found.')
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
x = MyLinkedList(2)
x.my_append(3)
x.my_append(5)
x.my_append(8)
x.my_append(14)
x.display()
x.my_search(8)
x.my_search(50)
x.my_remove(14)
x.display()
x.my_remove(50)