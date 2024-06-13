# board = []
# for i in range(9):
#     board.append(list(map(int, input().split())))

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]


# print(nums)
def isValue(board, i, j, k):
    """判断k放在board[i][j]是否合法"""
    # 行判断
    if k in board[i]:
        return False
    # 列判断
    columns = [m[j] for m in board]
    if k in columns:
        return False
    # 九宫格判断
    matrix = []
    i0 = 3*(i//3)
    j0 =3*(j//3)
    for m in range(i0, i0+3):
        for n in range(j0, j0+3):
            if k == board[m][n]:
                return False
    return True


def isTrue(board):
    """棋盘是否排满"""
    for i in board:
        if "." in i:
            return False
    return True


def backtracking(board):
    if isTrue(board):
        return True

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for k in range(1, 10):
                    if isValue(board, i, j, str(k)):
                        board[i][j] = str(k)
                        if backtracking(board):
                            return True
                        board[i][j] = "."  # 回溯
                return False

    return False


flag = backtracking(board)
# print(board)
print(flag)
for m in board:
    for i in m:
        print(i, end=" ")
    print()