class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >=self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data


    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.head.next is None:
            self.tail = new_node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.tail.prev is None:
            self.head = new_node
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index <=0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            curr = self.head
            for _ in range(index):
                curr = curr.next
            new_node.prev = curr.prev
            new_node.next = curr
            curr.prev.next = new_node
            curr.prev = new_node
            self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            if curr.prev is not None:
                curr.prev.next = curr.next
            else:
                self.head = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            else:
                self.tail = curr.prev
        self.size -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)