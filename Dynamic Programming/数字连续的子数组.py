"""
一、题目
    给定长度是N的数组array[0,....,n-1],求递增且连续数字最长的子数组。
    例如： 数组array=[1,2,3,34,56,57,58,59,60,61,99,121]的连续数字
    最长的一段为56 57 58 59 60 61

二、思路：动态规划
    定义：dp[i]存的是以array[i]结尾的最长连续递增子数组的长度
"""


def max_sequence_len(array):
    size = len(array)
    dp = [1] * size
    m = 1  # 记录最大的长度
    for i in range(1, size):
        if array[i] - array[i - 1] == 1:
            dp[i] += dp[i - 1]
            m = max(dp[i], m)
    return m


def max_sequence(array):
    size = len(array)
    dp = [1] * size  # dp[i]全部初始化为1
    m = 1  # 记录最大的长度
    index = 0
    for i in range(1, size):
        if array[i] - array[i - 1] == 1:
            dp[i] += dp[i - 1]
            m = max(dp[i], m)
            if m == dp[i]:
                index = i
    return m, array[index - m + 1:index + 1]


if __name__ == '__main__':
    array = [1, 2, 3, 54, 55, 56, 57, 58, 59, 60, 99, 121]
    print(max_sequence(array))
