"""
题目：
    给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，
    其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:
    输入:
        [1,2,3]
    输出:
        2
    说明：
        只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：
        [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

思路:
    要想将数组中所有元素都移动为相同的，而且总移动步数还得最小。必须将所有的数往数组的"中位数"移动.
    [将所有数往“平均数”移动的想法是错误，平均值容易受到异常点的影响，例如，实操一下数组[1,1,1,1,1,1000]，即可明白]
    本题的难点就是如何快速找到数组的中位数了，可以联想到“L_找出n个数里最小的k个”一题。中位数就是第(len(nums) >> 1)+1个数了。
    在逐个统计每个数与中位数的距离了，累加起来即可

注意：
    此代码Python版在LeetCode上超时，Java版的不超时
    leetcode-462题
"""


def min_moves(nums):
    k = (len(nums) >> 1) + 1
    median = find_min_k_th(nums, k)
    count = 0
    for num in nums:
        count += abs(num - median)
    return count


def find_min_k_th(nums, k):
    # 快速排序
    def quick_sort(nums, start, end, k):
        if start >= end:
            return
        pivot = nums[start]  # 基准值
        low = start
        high = end
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] < pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        if low == k - 1:
            return
        elif low < k - 1:
            quick_sort(nums, low + 1, end, k)
        else:
            quick_sort(nums, start, low - 1, k)

    quick_sort(nums, 0, len(nums) - 1, k)
    return nums[k - 1]


if __name__ == '__main__':
    print(min_moves([1, 2, 3]))
