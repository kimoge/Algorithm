class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        # 虚拟头结点
        self.head = Node()

    def get(self, index: int) -> int:
        cur = self.head
        while index >= 0 and cur.next is not None:
            cur = cur.next
            index -= 1
        if index != -1:
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        cur = self.head
        while index > 0:
            cur = cur.next
            if cur is None:
                return
            index -= 1
        newNode.next = cur.next
        cur.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        while index > 0:
            cur = cur.next
            if cur.next is None:
                return
            index -= 1
        cur.next = cur.next.next
