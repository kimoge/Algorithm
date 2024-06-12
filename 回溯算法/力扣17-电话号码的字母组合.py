ch_map = {"2": 'abc', "3": 'def', "4": 'ghi', "5": 'jkl', "6": 'mno', "7": 'pqrs', "8": 'tuv', "9": 'wxyz'}
digits = "23"


def backtracking(result, path, digits, level):
    if not digits:
        return
    if level == len(digits):
        result.append(path)
        return

    for i in ch_map[digits[level]]:
        backtracking(result, path + i, digits, level + 1)

res = []
backtracking(res, "", digits, 0)
print(res)