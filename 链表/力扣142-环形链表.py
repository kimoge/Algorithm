class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = [3,2,0,-4]
pos = 1
head_link = ListNode(head[0])
cur = head_link
for i in head[1:]:
    cur.next = ListNode(i)
    cur = cur.next

pre = head_link
while pos > 0:
    pre = pre.next
    pos -= 1
cur.next = pre
# print(cur.val)


# 不可执行的代码
fast = head_link
low = head_link
pre = head_link
while fast and fast.next:
    fast = fast.next.next
    low = low.next
    if fast is low:
        break

if fast is None or fast.next is None:
    print(None)

while pre is not low:
    low = low.next
    pre = pre.next

print(low.val)
