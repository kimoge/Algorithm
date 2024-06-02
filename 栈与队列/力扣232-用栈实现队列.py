class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.empty():
            if len(self.stack_out) == 0:
                while len(self.stack_in) != 0:
                    self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        if not self.empty():
            res = self.pop()
            self.stack_out.append(res)
            return res

    def empty(self) -> bool:
        if len(self.stack_in) + len(self.stack_out) == 0:
            return True
        else:
            return False
