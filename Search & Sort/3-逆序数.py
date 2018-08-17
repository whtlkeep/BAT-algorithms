"""
一、逆序数：
    给定一个数组array[0,...,n-1], 若对于某两个元素array[i],array[j],若i<j and array[i]>array[j],
    则认为array[i],array[j]是逆序对。一个数组中包含的逆序对的数目称为该数组的逆序数。设计一个算法求一个数组的逆序数
二、利用 归并排序 的思想
    在归并排序中，会将两个升序的数组进行合并，利用升序数组的特性，可以快速求得逆序数
    见 图解
"""

temp = [0] * 100
count = [0]
pairs = []


def Merge(nums, low, mid, high):
    i = low
    j = mid + 1
    size = 0
    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            temp[size] = nums[i]
            i += 1
        else:
            # 除了以下三行代码，其余代码与归并排序一模一样
            count[0] += (mid - i + 1)
            for h in range(i, mid + 1):
                pairs.append((nums[h], nums[j]))
            temp[size] = nums[j]
            j += 1
        size += 1
    while i <= mid:
        temp[size] = nums[i]
        size += 1
        i += 1
    while j <= high:
        temp[size] = nums[j]
        size += 1
        j += 1
    for i in range(size):
        nums[low + i] = temp[i]


def Merge_sort(nums, low, high):
    if low >= high:
        return
    mid = (low + high) >> 1
    Merge_sort(nums, low, mid)
    Merge_sort(nums, mid + 1, high)
    Merge(nums, low, mid, high)


if __name__ == '__main__':
    nums = [3, 56, 2, 7, 45, 8, 1]
    Merge_sort(nums, 0, len(nums) - 1)
    print(pairs)
