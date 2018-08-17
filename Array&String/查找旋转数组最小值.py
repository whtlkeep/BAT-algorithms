# coding:utf-8

"""
一、题目
0124567 --旋转--> 4567012 , 最小值 是 0

二、思路
用索引start, end 分别指向首尾元素，元素不重复。
    1、若子数组是普通升序数组，则 Array[start] < Array[end];  eg:Array = [4,5,6]
    2、若子数组是循环升序数组，前半段子数组的元素全都大于后半子数组中的元素：Array[start] > Array[end].  eg: Array = [7,0,1,2]

三、步骤：
计算中间位置 mid = (start + end) >> 1
    1、显然，Array[start...mid] 和 Array[mid+1....end]必有一个是循环升序数组，有一个是普通升序数组；
    2、若，Array[mid] > Array[end],说明子数组Array[mid+1,mid+2,...,end]是循环升序，更新 start = mid + 1
    3、若，Array[mid]<Array[end], 说明子数组Array[mid+1,mid+2,...,end]是普通升序， 更新 end = mid
"""


def findmin(array):
    size = len(array)
    low = 0
    high = size - 1
    while low < high:
        mid = (low + high) >> 1
        if array[mid] < array[high]:
            high = mid
        elif array[mid] > array[high]:
            low = mid + 1
    return array[low]


if __name__ == '__main__':
    array = [4, 5, 6, 7, 0, 1, 2]
    print(findmin(array))
