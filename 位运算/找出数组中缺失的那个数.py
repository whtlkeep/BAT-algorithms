"""
一、题目
    给定一个包含 0, 1, 2, ..., n 中 n 个数的序列nums，
    找出 0 .. n 中没有出现在序列中的那个数。

二、题意理解
    序列 0,1,2，...,n 一共有n+1个数，任意选择其中n个数生成一个序列，求未被选择的数字

三、思路
    * 排序后，挨个判断哪个数没有，即为所求。 时间复杂度O(NlogN)
    * 利用本题的数组是从0,1,2,..,n 中选择的n个数，数组nums的index是 0,1,2,3,...,n-1，加上数组的长度n.
        index 和 长度 构成了 0,1,2,3，...,n 一共 n+1 个数， 再加上nums中的数正好构成了2*n+1个数
        其中n个数出现了2次，1个数出现了1次，只出现一次的数就是缺少的数。 有木有很神奇！！！
        解法同“数组中唯一一个不重复的元素”
"""


def missing_number(nums):
    ret = 0
    size = len(nums)
    for i in range(size):
        ret = ret ^ i ^ nums[i]
    ret = ret ^ size
    return ret


if __name__ == '__main__':
    nums = [1, 2, 0, 4, 5]
    print(missing_number(nums))  # output:3
