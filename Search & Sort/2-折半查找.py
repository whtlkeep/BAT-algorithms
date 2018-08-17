#  本方法是 a 在nums中，则返回对应的index
def binary_find1(nums, a):
    size = len(nums)
    start = 0
    end = size - 1
    bFind = False
    middle = 0
    while start <= end:
        middle = (start + end) >> 1
        if nums[middle] == a:
            bFind = True
            break
        if nums[middle] > a:
            end = middle - 1
        else:
            start = middle + 1
    if bFind:
        return middle
    return -1


# 本方法是通过二分查找找到k在arr中插入位置，并插入
# 例如 arr = [1,2,3,4,5], k = 3.5, 则将k插入到4的位置，变成 arr = [1,2,3,3.5,5]
def binary_search2(arr, k):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) >> 1
        if arr[mid] == k:
            arr[mid] = k
            return arr
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    if arr[mid] < k and arr[mid + 1] > k:
        arr[mid + 1] = k
        return arr
    if arr[mid] > k and arr[mid - 1] < k:
        arr[mid] = k
        return arr


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    a = 4
    print(binary_find1(array, 1))
