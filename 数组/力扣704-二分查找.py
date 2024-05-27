nums = [-1, 0, 3, 5, 9, 12]
target = 9

l = 0
r = len(nums)-1
index = - 1
while l <= r:
    mid = (l+r)//2
    if nums[mid] < target:
        l = mid + 1
    if nums[mid] > target:
        r = mid - 1
    if nums[mid] == target:
        index = mid
        break
print(index)
