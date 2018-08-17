"""
一、题目
    找出n个数中最小的k个数
二、思路
    题目联想--“找出n个数中第k小的数”
    解法是：利用快速排序，每次调整后，会有一个基准值在正确的位置上，将基准值的index和k进行比较，
          找到第k小的值。
    对于本题，如果能找到第k小的值，则 数组的左边k个数 便是最小的k个数
"""


def find_min_topk(array, k):
    # 快速排序
    def quick_sort(alist, start, end, k):
        if start >= end:
            return
        pivot = alist[start]  # 基准值
        low = start
        high = end
        while low < high:
            while low < high and alist[high] >= pivot:
                high -= 1
            alist[low] = alist[high]
            while low < high and alist[low] < pivot:
                low += 1
            alist[high] = alist[low]
        alist[low] = pivot
        if low == k - 1:
            return
        elif low < k - 1:
            quick_sort(alist, low + 1, end, k)
        else:
            quick_sort(alist, start, low - 1, k)

    quick_sort(array, 0, len(array) - 1, k)
    result = [i for i in sorted(array[0:k])]
    return result


if __name__ == '__main__':
    array = [1, 2, 3, -1, 2, 199, 100]
    print(find_min_topk(array, 5))
