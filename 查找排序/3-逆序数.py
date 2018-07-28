"""
一、逆序数：
    给定一个数组array[0,...,n-1], 若对于某两个元素array[i],array[j],若i<j and array[i]>array[j],
    则认为array[i],array[j]是逆序对。一个数组中包含的逆序对的数目称为该数组的逆序数。设计一个算法求一个数组的逆序数
二、利用 归并排序 的思想
    在归并排序中，会将两个升序的数组进行合并，利用升序数组的特性，可以快速求得逆序数
"""

temp = [0] * 100


def Merge(array, low, mid, high, count):
    i = low
    j = mid + 1
    size = 0
    while i <= mid and j <= high:
        if array[i] < array[j]:
            temp[size] = array[i]
            i += 1
        else:
            count += (mid - i + 1)
            temp[size] = array[j]
            j += 1
        size += 1
    while i <= mid:
        temp[size] = array[i]
        size += 1
        i += 1
    while j <= high:
        temp[size] = array[j]
        size += 1
        j += 1
    for i in range(size):
        array[low + i] = temp[i]


def Merge_sort(array, low, high, count):
    if low >= high:
        return
    mid = (low + high) >> 1
    Merge_sort(array, low, mid, count)
    Merge_sort(array, mid + 1, high, count)
    Merge(array, low, mid, high, count)


if __name__ == '__main__':
    count = 0
    array = [3, 56, 2, 7, 45, 8, 1]
    Merge_sort(array, 0, len(array) - 1, count)
    print(count)
