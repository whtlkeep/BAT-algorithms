"""
题目：
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
    请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
    你可以假设 nums1 和 nums2 均不为空。
"""


def find_median_from_one_sorted_array(nums):
    size = len(nums)
    if size % 2 == 1:
        return nums[size >> 1]
    else:
        mid = (size - 1) >> 1
        return (nums[mid] + nums[mid + 1]) / 2


def find_median_from_two_sorted_array(nums1, nums2):
    size1 = len(nums1)
    size2 = len(nums2)
    if size1 == 0:
        return find_median_from_one_sorted_array(nums2)
    if size2 == 0:
        return find_median_from_one_sorted_array(nums1)
    start1, end1 = 0, size1 - 1
    start2, end2 = 0, size2 - 1
    while True:
        if start1 > end1:
            return find_median_from_one_sorted_array(nums2[start2: end2 + 1])
        elif start2 > end2:
            return find_median_from_one_sorted_array(nums1[start1: end1 + 1])
        mid1 = (start1 + end1) >> 1
        mid2 = (start2 + end2) >> 1
        if start1 == end1 and start2 == end2:
            return (nums1[mid1] + nums2[mid2]) / 2
        elif start1 != end1 and start2 != end2:
            move_step = min(end1 - start1 + 1, end2 - start2 + 1) >> 1
            if nums1[end1] > nums2[end2]:
                end1 -= move_step
            else:
                end2 -= move_step

            if nums1[start1] < nums2[start2]:
                start1 += move_step
            else:
                start2 += move_step
        else:
            if start2 == end2:
                nums1, nums2 = nums2, nums1
                start1, start2 = start2, start1
                end1, end2 = end2, end1
                mid1, mid2 = mid2, mid1
            print(nums1, nums2)
            if (end2 - start2 + 1) % 2 == 0:  # 偶数
                if nums1[mid1] < nums2[mid2]:
                    return nums2[mid2]
                elif nums1[mid1] > nums2[mid2 + 1]:
                    return nums2[mid2 + 1]
                else:
                    return nums1[mid1]
            else:
                if nums1[mid1] > nums2[mid2 + 1]:
                    return (nums2[mid2] + nums2[mid2 + 1]) / 2
                elif nums1[mid1] < nums2[mid2 - 1]:
                    return (nums2[mid2] + nums2[mid2 - 1]) / 2
                else:
                    return (nums1[mid1] + nums2[mid2]) / 2


if __name__ == '__main__':
    print(find_median_from_two_sorted_array([1, 3], [2]))
