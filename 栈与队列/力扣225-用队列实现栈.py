from collections import deque
class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if not self.empty():
            while len(self.queue_in) != 1:
                self.queue_out.append(self.queue_in.popleft())
            # 此时queue_in 只剩要pop的元素
            # 交换in和out，使in只用来接受push的元素，out只有在执行pop操作时才保存一个要pop元素，之后out队列仍为空
            self.queue_in, self.queue_out = self.queue_out, self.queue_in
            return self.queue_out.popleft()

    def top(self) -> int:
        if not self.empty():
            res = self.pop()
            self.push(res)
            return res

    def empty(self) -> bool:
        return len(self.queue_in) == 0
