nums = [1,7,4,9,2,5]

# 计算峰个数
sub_length = 0

if len(nums) == 1:
    sub_length = 1

else:
    pre_diff = 0
    cur_diff = 0
    sub_length = 1
    # 找峰个数
    for i in range(0, len(nums)-1):
        cur_diff = nums[i+1] - nums[i]
        if (pre_diff <= 0 and cur_diff > 0) or (pre_diff >= 0 and cur_diff < 0):
            sub_length += 1
            # 找到峰值再更新
            pre_diff = cur_diff

print(sub_length)