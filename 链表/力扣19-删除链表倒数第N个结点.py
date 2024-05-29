class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = [1,2,3,4]
n = 2

head_link = ListNode(head[0])
cur = head_link
for i in head[1:]:
    cur.next = ListNode(i)
    cur = cur.next


head_virtual = ListNode()
head_virtual.next = head_link


fast = head_link
low = head_link
while n > 0:
    fast = fast.next
    n -= 1

while fast.next:
    fast = fast.next
    low = low.next

low.next = low.next.next
