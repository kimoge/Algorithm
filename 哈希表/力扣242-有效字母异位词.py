s = "anagram"
t = "nagaram"
arr = [0] * 26
for i in s:
    arr[ord(i)-ord("a")] += 1
for i in t:
    arr[ord(i)-ord("a")] -= 1

for i in range(26):
    if arr[i] != 0:
        print("false")
        break
