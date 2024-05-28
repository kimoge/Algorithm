class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = [1,2,6,3,4,5,6]
val = 6

# 创建链表
head_link = ListNode(head[0])
cur = head_link
for i in head[1:]:
    cur.next = ListNode(i)
    cur = cur.next

# # 1、使用虚拟头节点
# head_virtual = ListNode()
# head_virtual.next = head_link
#
# # 对cur.next进行判断
# cur = head_virtual
# while cur.next is not None:
#     if cur.next.val == val:
#         cur.next = cur.next.next
#     else:
#         cur = cur.next

# 2、不适用虚拟头结点
while head_link.val == val:
    head_link = head_link.next

cur = head_link
while cur is not None and cur.next is not None:
    if cur.next.val == val:
        cur.next = cur.next.next
    else:
        cur = cur.next


