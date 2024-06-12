str = "abbc"


def isTrue(str0, start, end):
    s0 = list(str0[start:end+1])
    s1 = list(reversed(s0))
    if s0 == s1:
        return True
    return False


def backtracking(arr, path, str0, start_index):
    if start_index >= len(str0):
        arr.append(path)

    for i in range(start_index, len(str0)):
        if isTrue(str0, start_index, i):
            backtracking(arr, path + [str0[start_index:i+1]], str0, i+1)

arr = []
backtracking(arr, [], str, 0)
print(arr)