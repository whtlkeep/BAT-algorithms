"""
题目：
    给定一个数组A[0....N-1], 找到从1开始，第一个不再数组中的正整数
    如 [3,5, 1, 2, -3, 7, 14, 8] 输出4

思路：
    对数组中的元素进行不断交换，使得元素都满足A[i] == i。交换完后，第一个不满足该等式的便是缺失值！  【下标从 1 开始】
    有一个思想--假如数组A的长度是size,缺失值只有两种可能：
        一、在[1,size]闭区间内
        二、等于size+1。出现这可能的情况是数组A是形如[1,2,3,4,5,...]从1开头的连续数组
    接下来的思想：
        * 不断将数字放在正确的位置（A[i] == i）上
        * 将不在有效区间[1,size]的数字舍弃，更新size的大小
        * 将重复出现的数字也舍弃，更新size的大小
"""


def first_miss_number(nums):
    size = len(nums)
    nums.insert(0, -1)  # 在数组前面添加一个元素，这样原来数字的下标从 1 开始，便于计算
    i = 1
    while i <= size:
        if nums[i] == i:
            i += 1
        # 数字小于下标      数字大于理论的最大值      数字存在重复            --> 都舍弃，理论最大值减一
        elif nums[i] < i or nums[i] > size or nums[i] == nums[nums[i]]:
            nums[i] = nums[size]
            size -= 1
        elif nums[i] > i:  # 当前数字比下标要大，则交换
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        else:
            pass
    return i


if __name__ == '__main__':
    print(first_miss_number([3, 5, 1, 2, -3, 7, 4, 8]))
    print(first_miss_number([2, 3, 4, 5, 6, 7]))
    print(first_miss_number([1, 2, 3, 4]))
