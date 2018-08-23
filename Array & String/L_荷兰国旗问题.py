"""
一、题目
    现有红、白、蓝三个不同颜色的小球，乱序排序在一起，
    请重新排列这些小球，使得红白蓝三色的同颜色的球在一起。

二、问题转换：
    给定数组array[0,...n-1],元素只能取0,1,2三个值，设计算法，
    使得数组排列成“0000...00001111....11112222...2222”

三、解题思路：
    * 借鉴快速排序中partition的过程
    * 初始化： begin = 0，cur = 0，end = N-1
    * 打算[0,begin)全是0, [begin,cur)全是1,
      [cur,end)是未遍历的数, [end,size-1)全是2
四、解题步骤：
    * if array[cur] = 2, then swap(cur, end), end--
    * if array[cur] =1, then cur++
    * if array[cur] = 0, then ：
        * if begin == cur, then begin++, cur++
        * if begin != cur, then swap(cur,begin), begin++,cur++
"""


def hollandr(nums):
    size = len(nums)
    begin = 0
    cur = 0
    end = size - 1
    while cur <= end:
        if nums[cur] == 2:
            nums[cur], nums[end] = nums[end], nums[cur]
            end -= 1
        elif nums[cur] == 1:
            cur += 1
        else:
            if cur != begin:
                nums[cur], nums[begin] = nums[begin], nums[cur]
            begin += 1
            cur += 1


if __name__ == '__main__':
    nums = [1, 2, 0, 0, 0, 1, 0, 2, 0, 1, 0, 1, 1, 1, 1, 0, 1]
    hollandr(nums)
    print(nums)
