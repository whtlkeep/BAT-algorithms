"""
题目：
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2]
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(logN) 级别。

示例：
    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4

    输入: nums = [4,5,6,7,0,1,2], target = 3
    输出: -1

思路：
    用索引start, end 分别指向首尾元素，元素不重复。
    1、若子数组是普通升序数组，则 Array[start] < Array[end];  eg:Array = [4,5,6]
    2、若子数组是循环升序数组，前半段子数组的元素全都大于后半子数组中的元素：Array[start] > Array[end].  eg: Array = [7,0,1,2]

步骤：
    计算中间位置 mid = (start + end) >> 1
    1、显然，Array[start...mid] 和 Array[mid+1....end]必有一个是循环升序数组，有一个是普通升序数组
    2、若，Array[mid] > Array[end],说明子数组Array[mid+1,mid+2,...,end]是循环升序，Array[start,...,mid]是普通升序数组：
        先判断target是否在普通升序中，否则在循环升序数组中
    3、若，Array[mid]<Array[end], 说明子数组Array[mid+1,mid+2,...,end]是普通升序，Array[start,...,mid]是循环升序数组：
        先判断target是否在普通升序中，否则在循环升序数组中
"""


def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[high]:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        elif nums[mid] > nums[high]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            break
    return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 7, 0, 1, 2], 100))
