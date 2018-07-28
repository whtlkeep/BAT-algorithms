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


datas = input().split()
k = int(datas[-1])
nums = [int(i) for i in datas[0:-1]]
quick_sort(nums, 0, len(nums) - 1, k)
result = [str(i) for i in sorted(nums[0:k])]
print(" ".join(result))
