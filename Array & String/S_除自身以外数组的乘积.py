"""
题目：
    给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
    其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
    输入: [1,2,3,4]
    输出: [24,12,8,6]
    说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
    
思路：
    本题难点在于 不许使用除法。
    其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积，
    即 output[i] = nums[0] * nums[1] * ... * nums[i-1] * nums[i+1] * ... * nums[size-1],
    要想实现连乘，只能采用构造的方法：将数组从左往右遍历，从右往左遍历，不断累加相乘，对每一个output[i]构成出满足条件的乘法因子。
"""


def product_except_self(nums):
    size = len(nums)
    output = [1] * size
    left = 1
    for i in range(1, size):
        left *= nums[i - 1]
        output[i] *= left
    right = 1
    for j in range(size - 2, -1, -1):
        right *= nums[j + 1]
        output[j] *= right
    return output


if __name__ == '__main__':
    print(product_except_self([1, 2, 3, 4]))
