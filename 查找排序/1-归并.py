"""
一、介绍
   基本思想：
   将数组array[0,...,n-1]中的元素分成两个子数组：array1[0,...,n/2]
   和array2[n/2+1,...,n-1]。分别对这两个数组单独排序，然后将已排序的
   两个子数组归并成一个含有n个元素的有序数组

二、步骤
    递归实现

三、时间复杂度：O(N*logN)

四、归并排序的两点改进
    * 在数组长度比较短的情况下，不进行递归，而是选择其他排序方案，如插入排序
    * 归并过程中，可以用记录数组下标的方式代替申请新内存空间；从而避免array和
      辅助数组间的频繁数据移动
"""
def merge(left, right):  # 合并两个有序数组
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    num = len(alist) >> 1
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    return merge(left, right)

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    result = merge_sort(alist)
    print(result)