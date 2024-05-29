class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = [1,2,3,4,5]

# 创建链表
head_link = ListNode(head[0])
cur = head_link
for i in head[1:]:
    cur.next = ListNode(i)
    cur = cur.next


pre = None
cur = head_link
while cur is not None:
    temp = cur.next
    cur.next = pre
    pre = cur
    cur = temp

head_link = pre


