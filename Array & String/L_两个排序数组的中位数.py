"""
题目：
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
    请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
    你可以假设 nums1 和 nums2 均不为空。
"""


def find_median_sorted_arrays(nums1, nums2):
    size = len(nums1) + len(nums2)
    mid = size >> 1
    if size % 2 == 1:
        return find_k_th(nums1, nums2, mid + 1)
    else:
        smaller = find_k_th(nums1, nums2, mid)
        bigger = find_k_th(nums1, nums2, mid + 1)
        return (smaller + bigger) / 2.0


def find_k_th(nums1, nums2, k):
    if len(nums1) == 0:
        return nums2[k - 1]
    if len(nums2) == 0:
        return nums1[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])
    mid = k >> 1
    a = nums1[mid - 1] if len(nums1) >= mid else None
    b = nums2[mid - 1] if len(nums2) >= mid else None
    if b is None or (a is not None and a < b):
        return find_k_th(nums1[mid:], nums2, k - mid)
    return find_k_th(nums1, nums2[mid:], k - mid)


if __name__ == '__main__':
    print(find_median_sorted_arrays([1, 2, 3, 10], [4, 5, 6, 7]))
    print(find_k_th([1, 2, 3, 10], [4, 5, 6, 7], 8))
