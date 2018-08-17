# coding:utf-8
"""
对于两个子序列 S1 和 S2，找出它们最长的公共子序列。

定义一个二维数组 dp 用来存储最长公共子序列的长度，其中 dp[i][j] 表示 S1 的前 i 个字符与 S2 的前 j 个字符最长公共子序列的长度。
考虑 S1i 与 S2j 值是否相等，分为两种情况：

当 S1i==S2j 时，那么就能在 S1 的前 i-1 个字符与 S2 的前 j-1 个字符最长公共子序列的基础上再加上 S1i 这个值，
最长公共子序列长度加 1 ，即 dp[i][j] = dp[i-1][j-1] + 1。
当 S1i != S2j 时，此时最长公共子序列为 S1 的前 i-1 个字符和 S2 的前 j 个字符最长公共子序列，
与 S1 的前 i 个字符和 S2 的前 j-1 个字符最长公共子序列，它们的最大者，即 dp[i][j] = max{ dp[i-1][j], dp[i][j-1] }。
综上，最长公共子序列的状态转移方程为：


对于长度为 N 的序列 S1 和 长度为 M 的序列 S2，dp[N][M] 就是序列 S1 和序列 S2 的最长公共子序列长度。

与最长递增子序列相比，最长公共子序列有以下不同点：

针对的是两个序列，求它们的最长公共子序列。
在最长递增子序列中，dp[i] 表示以 Si 为结尾的最长递增子序列长度，子序列必须包含 Si ；
在最长公共子序列中，dp[i][j] 表示 S1 中前 i 个字符与 S2 中前 j 个字符的最长公共子序列长度，不一定包含 S1i 和 S2j 。
在求最终解时，最长公共子序列中 dp[N][M] 就是最终解，而最长递增子序列中 dp[N] 不是最终解，
因为以 SN 为结尾的最长递增子序列不一定是整个序列最长递增子序列，需要遍历一遍 dp 数组找到最大者。

https://github.com/CyC2018/Interview-Notebook/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3.md#%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92
"""


def lengthofLCS(nums1, nums2):
    dp = []
    len1, len2 = len(nums1), len(nums2)
    for i in range(len1 + 1):
        row = []
        for j in range(len2 + 1):
            row.append(0)
        dp.append(row)
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i = len1
    j = len2
    sub = []
    while i != 0 and j != 0:
        if nums1[i - 1] == nums2[j - 1]:
            sub.append(nums1[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                j -= 1
            else:
                i -= 1
    return dp[len1][len2], sub[::-1]


nums1 = ['a', 'b', 'c', 'b', 'd', 'a', 'b']
nums2 = ['b', 'd', 'c', 'a', 'b', 'a']
print(lengthofLCS(nums1, nums2))
