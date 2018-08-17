"""
一、题目
给定一个数组array[0,1,...,n-1]，求array的连续子数组，使得该子数组的和最大

二、思路：动态规划
dp[i]为以array[i]结尾的数组中和最大的子数组
"""


# 求得最大值
def max_sub_array_sum(array):
    if array == None:
        return 0
    size = len(array)
    if size == 0:
        return 0
    sum_ = array[0]  # 当前子串的和
    result = sum_  # 当前找到的最优解
    for a in array[1:]:
        if sum_ > 0:
            sum_ += a
        else:
            sum_ = a
        result = max(sum_, result)
    return result


# 求得最大连续子数组本身
def max_sub_array(array):
    if array == None:
        return 0
    size = len(array)
    if size == 0:
        return 0
    start, end = 0, 0
    sum_ = array[0]
    result = sum_  # 最大和
    for i, a in enumerate(array[1:]):
        if sum_ > 0:
            sum_ += a
        else:
            sum_ = a
            startNew = i + 1
        if result < sum_:
            result = sum_
            start = startNew
            end = i + 1
    return array[start:end + 1], result


if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5, 6]
    print(max_sub_array(array))
