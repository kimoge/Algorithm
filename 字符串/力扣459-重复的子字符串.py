s = "aba"

new_s = s*2
new_s = new_s[1:-1]
# str.find() KMP算法查找，O（n+m）
if new_s.find(s) != -1:
    print(True)
else:
    print(False)
