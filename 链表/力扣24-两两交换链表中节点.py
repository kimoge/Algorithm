class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = [1,2,3,4]

head_link = ListNode(head[0])
cur = head_link
for i in head[1:]:
    cur.next = ListNode(i)
    cur = cur.next


head_virtual = ListNode()
head_virtual.next = head_link

cur = head_virtual
while cur.next and cur.next.next:
    n1 = cur.next
    n2 = n1.next.next
    cur.next = n1.next
    cur.next.next = n1
    n1.next = n2

    cur = n1

