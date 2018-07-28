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


def two_sum1(array, s):

    def quick_sort(alist, start, end):  # 快速排序
        if start >= end:
            return
        pivot = alist[start]  # 基准值
        low = start  # 左指针
        high = end  # 右指针
        while low < high:
            while low < high and alist[high] >= pivot:
                high -= 1
            alist[low] = alist[high]

            while low < high and alist[low] < pivot:
                low += 1
            alist[high] = alist[low]
        alist[low] = pivot
        quick_sort(alist, start, low - 1)
        quick_sort(alist, low + 1, end)

    quick_sort(array, 0, len(array) - 1)
    size = len(array)
    start = 0
    end = size - 1
    result = []
    while start < end:
        if array[start] + array[end] < s:
            start += 1
        elif array[start] + array[end] > s:
            end -= 1
        else:
            result.append([array[start], array[end]])
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
            result.append([a, s-a])
            del hashh[a]
    return result

if __name__ == '__main__':
    array = [0, 3, 7, 9, 10, 11, 14, 16, 17]
    print(two_sum2(array, 1))