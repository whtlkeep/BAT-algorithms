"""
使用二分查找，在有序数组找到指定元素的位置
"""
def binary_search(arr,k):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end) >> 1
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            start = mid+1
        else:
            end = mid - 1
    if arr[mid]<k and arr[mid+1]>k:
        return mid + 1
    if arr[mid]>k and arr[mid-1]<k:
        return mid

arr = [1,2,3,4,5]
print(binary_search(arr,3.5))