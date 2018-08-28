class Node():
    def __init__(self, val, next_node):
        self.val = val
        self.next_node = next_node


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        if self.length == 0:
            return -1
        if (index+1)> self.length or index < 0:
            return -1
        start = 0
        curr = self.head
        while start != index:
            start += 1
            curr = curr.next_node
        return curr.val

    def addAtHead(self, val):

        if not self.head:
            node = Node(val, None)
            self.head = node
            self.length += 1
        else:
            in_node = Node(val, self.head)
            self.head = in_node
            self.length += 1

    def addAtTail(self, val):
        node = Node(val, None)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next_node:
                temp = temp.next_node
            temp.next_node = node
        self.length += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        in_node = Node(val, None)
        node = self.head
        count = 0
        while True:
            if count == (index-1):
                temp = node.next_node
                node.next_node = in_node
                in_node.next_node = temp
                self.length += 1
                return
            count += 1
            node = node.next_node

    def deleteAtIndex(self, index):
        if self.length == 0:
            return
        if index < 0 or index >= self.length:
            return
        node = self.head
        count = 0
        while node.next_node:
            count += 1
            if index == count:
                node.next_node = node.next_node.next_node
                break
            node = node.next_node
        self.length -= 1


