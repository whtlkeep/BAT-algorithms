"""
题目：
    归并两个有序数组nums1,nums2，并要求将nums2归并到nums1上

示例：
    nums1 = [1,2,3], nums2=[2,5,6] ,得 nums1 = [1,2,2,3,5,6]

思路：
    如果不做任何要求，归并两个有序数组可以直接申请一个新的list，将nums1和nums2中的数组逐个移动过去即可；
    而本题要求必须归并到nums1中，这样在操作过程中需要不断移动nums1的数据。要想移动不出错，则需要记录从nums2中插入的数据个数。

    从前往后的归并，会出现nums1中的数被多次后移，比较复杂。
    可以逆向思考，先在nums1后面接上长度为nums2的空间，在从后往前归并，这样每个数只会被移动一次
"""


def merge(nums1, nums2):
    end1 = len(nums1) - 1  # 原nums1的尾指针
    end2 = len(nums2) - 1  # 原nums2的尾指针

    nums1 = nums1 + [0] * (end2 + 1)
    index = len(nums1) - 1  # 新nums1的尾指针
    # 从后往前，将nums2归并到nums1中
    while index >= 0:
        if end2 < 0:  # 表示 nums2 上的数已经全部归并到 nums1 上
            break
        if end1 < 0:  # 表示 nums1 上的数比较小，已经全部被后移
            nums1[index] = nums2[end2]
            end2 -= 1
            index -= 1
            continue
        # 取较大的值放在nums1[index]上
        if nums1[end1] >= nums2[end2]:
            nums1[index] = nums1[end1]
            end1 -= 1
        else:
            nums1[index] = nums2[end2]
            end2 -= 1
        index -= 1
    del nums2
    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [1, 1, 1]
    print(merge(nums1, nums2))
