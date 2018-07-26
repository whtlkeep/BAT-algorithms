"""
求局部最大值
给定一个无重复元素的数组A，求找到一个该数组的局部最大值
满足条件：a[i]>a[i-1] and a[i]>a[i+1] , a[i]是局部最大值
"""
def localmaximum(array):
    start = 0
    end = len(array) - 1
    while start < end:
        mid = (start + end) >> 1
        if array[mid] > array[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return array[start]

array = [1, 2, 1, 3, 1, 1, 1, 1, 9]
print(localmaximum(array))