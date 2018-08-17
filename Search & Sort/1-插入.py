"""
------------------------------- 插入排序 --------------------------------------
一、介绍
    插入排序（英语：Insertion Sort）是一种简单直观的排序算法。

二、步骤
    通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
"""


def insert_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)
    print(alist)
