"""
------------------------------- 选择排序 --------------------------------------
一、介绍
    选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，
    存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    以此类推，直到所有元素均排序完毕。

二、步骤
    选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，
    它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。在所有的完全依靠交换
    去移动元素的排序方法中，选择排序属于非常好的一种。
"""


def selection_sort1(nums):
    # 思路是将最小值逐一选择到前面
    n = len(nums)
    for i in range(n - 1):
        min_index = i  # 记录最小值的位置
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]


def selection_sort2(nums):
    # 思路是将最大值逐一选择到后面
    n = len(nums)
    for i in range(n - 1, 0, -1):
        max_index = i  # 记录最大值的位置
        for j in range(i):
            if nums[j] > nums[max_index]:
                max_index = j

        if max_index != i:
            nums[i], nums[max_index] = nums[max_index], nums[i]


if __name__ == '__main__':
    nums = list(range(31,0,-1))
    selection_sort2(nums)
    print(nums)
