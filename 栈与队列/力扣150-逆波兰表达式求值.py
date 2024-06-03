tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


def is_num(s):
    try:
        int(s)
        return True
    except:
        return False


stack = []
for i in tokens:
    if is_num(i):
        stack.append(int(i))
    else:
        t0 = stack.pop()
        t1 = stack.pop()
        if i == "+":
            stack.append(t1 + t0)
        elif i == "-":
            stack.append(t1 - t0)
        elif i == "*":
            stack.append(t1 * t0)
        elif i =="/":
            stack.append(int(t1 / t0))

print(stack.pop())