"""
无重复 字符串的全排列  递归
array=[1,2,3,4],start是排列的起始位
"""


def permutation(nums, start=0):
    size = len(nums)
    if start == size - 1:
        print(nums)
        return
    for i in range(start, size):
        nums[i], nums[start] = nums[start], nums[i]
        permutation(nums, start + 1)
        nums[i], nums[start] = nums[start], nums[i]


# ---------------------- important --------------------------
"""
有重复 字符串的全排列  递归
array=[1,3,3,4],start是排列的起始位
"""


def permutation(nums, start=0):
    size = len(nums)
    if start == size - 1:
        print(nums)
        return
    dup = set()
    for i in range(start, size):
        if nums[i] in dup:
            continue
        dup.add(nums[i])
        nums[i], nums[start] = nums[start], nums[i]
        permutation(nums, start + 1)
        nums[i], nums[start] = nums[start], nums[i]


""" *******全排列的非递归算法*****************
    * 思路：
        起点：字典序最小的排列，例如 12345
        终点：字典序最大的排序，例如 54321
        过程：从当前排列生成字典序刚好比它大的下一个排列
    * 如何求字典序中一个排序的下一个排列？
        * 后找：字符串中最后一个升序的位置i, 即：
                string[k]>string[k+1](k>i),string[i]<string[i+1].i之后都是降序
        * 查找：string[i+1,...,n-1]中比string[i]大的最小值string[j]
        * 交换：swap(i,j)
        * 翻转：翻转string[i+1:n]

"""


def get_next_permutation(nums):
    size = len(nums)
    # 后找
    i = size - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i < 0:
        return False

    # 小大
    j = size - 1
    while nums[j] <= nums[i]:
        j -= 1

    # 交换
    nums[j], nums[i] = nums[i], nums[j]

    # 翻转
    reverse(nums, i + 1, size - 1)
    return True


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def permutation(nums):
    print(nums)
    while get_next_permutation(nums):
        print(nums)


# ---------------------- important --------------------------

array = list("1234")
permutation(array)
