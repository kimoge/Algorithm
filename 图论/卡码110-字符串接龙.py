from collections import deque
import string
import sys



if __name__ == '__main__':

    n = int(input())

    beginStr, endStr = input().split()

    strList = set()
    for i in range(n):
        strList.add(input())

    path = 0
    que = deque()
    que.append(beginStr)
    visited = {beginStr: 1}

    while que:
        cur_str = que.popleft()
        path = visited[cur_str]
        for i in range(len(cur_str)):
            for j in string.ascii_lowercase:
                new_str = cur_str[:i] + j + cur_str[i+1:]
                if new_str == endStr:
                    print(path + 1)
                    sys.exit()
                if new_str in strList and new_str not in visited.keys():
                    visited[new_str] = path + 1
                    que.append(new_str)
    print(0)
