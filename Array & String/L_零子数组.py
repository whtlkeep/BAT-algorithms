"""
一、题目
求长度为N的数组array，求连续子数组的和 最接近0的值

二、算法思想
    申请比array长1的空间 sum[-1,0,1,2,....,n-1], sum[i]是array的前i项和
    定义sum[-1] = 0
    显然有 array[i] + array[i+1]+....+array[j] = sum[j] - sum[i-1]

三、步骤
    对于sum[-1,0,...,n-1]排序，然后计算sum相邻元素的差的绝对值，最小值即为所求

"""


# 子数组的和最接近0，求这个数
def min_sub_array_num(nums):
    size = len(nums)
    sum_ = [0] * (size + 1)
    i = 1
    for a in nums:
        sum_[i] = sum_[i - 1] + a
        i += 1
    sum_ = sorted(sum_)
    difference = abs(sum_[1] - sum_[0])  # 差值
    result = difference
    for i in range(1, size):
        difference = abs(sum_[i + 1] - sum_[i])
        result = min(difference, result)
    del sum_
    return result


# 子数组的和最接近0，求这个子数组
# 利用字典存储一下每一个sum对应的index, 这样在排序后，可以利用index找出该子数组
def min_sub_array(nums):
    size = len(nums)
    sum_ = dict()
    for i in range(-1, size):
        sum_[i] = 0
    i = 0
    for a in nums:
        sum_[i] = sum_[i - 1] + a
        i += 1
    sum_ = sorted(sum_.items(), key=lambda d: d[1])
    difference = abs(sum_[1][1] - sum_[0][1])  # 差值
    result = difference
    start, end = 0, 0
    for i in range(1, size):
        difference = abs(sum_[i + 1][1] - sum_[i][1])
        result = min(difference, result)
        if result == difference:
            start = min(sum_[i + 1][0], sum_[i][0])
            end = max(sum_[i + 1][0], sum_[i][0])
    return result, nums[start + 1: end + 1]


if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5, 7, -4]
    print(min_sub_array(array))
