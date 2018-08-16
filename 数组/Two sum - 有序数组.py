"""
题目：
    在有序数组中找出两个数，使它们的和为 target。

思路： 双指针
    使用双指针，一个指针指向值较小的元素，一个指针指向值较大的元素。
    指向较小元素的指针从头向尾遍历，指向较大元素的指针从尾向头遍历。
    遍历过程：
        * 如果两个指针指向元素的和 sum == target，那么得到要求的结果；
        * 如果 sum > target，移动较大的元素，使 sum 变小一些；
        * 如果 sum < target，移动较小的元素，使 sum 变大一些。
"""


def two_sum(nums, target):
    size = len(nums)
    start = 0
    end = size - 1
    while start < end:
        temp = nums[start] + nums[end]
        if temp == target:
            return nums[start], nums[end]
        elif temp < target:
            start += 1
        else:
            end -= 1
    return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    print(two_sum(nums=nums,target=9))