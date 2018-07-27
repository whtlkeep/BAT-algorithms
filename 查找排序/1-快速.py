"""
一、介绍
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

二、步骤
    递归实现
"""

def quick_sort(alist, start, end):
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

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist)-1)
    print(alist)