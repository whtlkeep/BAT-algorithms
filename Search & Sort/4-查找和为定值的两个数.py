"""
寻找和为定值的两个数
给定N个 不同 的数A[0,...,N-1]以及某定值sum,找到这个N个数中的两个数，使得他们的和为sum

方法一：时间复杂度 O(N*logN)
    先将数组排序，然后用两个指针start,end 各自指向数组的首尾两端。
    步骤：
    * if a[start] + a[end] > sum, then end--
    * if a[start] + a[end] < sum, then start++
    * if a[start] + a[end] == sum, then 若果只输出一个结果，则break，否则，start++,end--

方法二：时间复杂度是O(N),空间复杂度是O(N)
"""


def two_sum1(nums, s):
    def quick_sort(nums, start, end):  # 快速排序
        if start >= end:
            return
        pivot = nums[start]  # 基准值
        low = start  # 左指针
        high = end  # 右指针
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]

            while low < high and nums[low] < pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        quick_sort(nums, start, low - 1)
        quick_sort(nums, low + 1, end)

    quick_sort(nums, 0, len(nums) - 1)
    size = len(nums)
    start = 0
    end = size - 1
    result = []
    while start < end:
        if nums[start] + nums[end] < s:
            start += 1
        elif nums[start] + nums[end] > s:
            end -= 1
        else:
            result.append([nums[start], nums[end]])
            start += 1
            end -= 1
    return result


def two_sum2(array, s):
    hashh = dict()
    for a in array:
        hashh[a] = None
    result = []
    for a in array:
        if s - a in hashh and s - a != a:
            result.append([a, s - a])
            del hashh[a]
    return result


if __name__ == '__main__':
    array = [0, 3, 7, 9, 10, 11, 14, 16, 17]
    print(two_sum2(array, 3))
