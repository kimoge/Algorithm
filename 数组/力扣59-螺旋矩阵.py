n = 5
matrix = [[0] * n for i in range(n)]
# 设置第一圈的起始位置
startx = 0
starty = 0
offset = 1
count = 1
# 设置转的圈数,规则遵循[)左闭右开
for m in range(n//2):
    for j in range(starty, n - offset):
        matrix[startx][j] = count
        count += 1

    j += 1  # 第一次循环结束后,j+1表示位于该圈末列
    for i in range(startx, n - offset):
        matrix[i][j] = count
        count += 1

    i += 1  # i在该圈末行
    for j in range(j, starty, -1):
        matrix[i][j] = count
        count += 1

    j -= 1  # j在该圈首列
    for i in range(i, startx, -1):
        matrix[i][j] = count
        count += 1
    i -= 1 # i在该圈首行，因为该圈循环结束可以不写

    offset += 1
    startx += 1
    starty += 1

if n%2 == 1:
    matrix[n//2][n//2] = count


# 输出结果
for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
