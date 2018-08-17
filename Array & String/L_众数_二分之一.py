"""
给定N个数，称出现次数最多的数为众数；若某众数出现的次数大于N/2，称改众数为绝对众数
A  = [1,2,1,3,1]  ， 1是绝对众数
"""


# 已知给定的数组存在绝对众数，求
def mode(nums):
    count = 0
    m = nums[0]
    for a in nums:
        if count == 0:
            m = a
            count = 1
        elif m != a:
            count -= 1
        else:
            count += 1
    return m


array = [8, 8, 1, 1, 1, 8, 1, 1, 6, 1, 8, 8, 8, 8]
print(mode(array))
