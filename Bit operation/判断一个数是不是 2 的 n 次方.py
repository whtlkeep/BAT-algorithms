"""
一、题目
    判断一个数是不是 2 的n 次方

二、思路
    满足条件的数的二进制中有且只有最左边的一位是1，其余都是0
"""


def isPowerOfTwo(num):
    # num & (num - 1)的意思是：8（1000）& 7（0111） = 0（0000），所有满足条件的数都满足这一性质
    return num > 0 and num & (num - 1) == 0


if __name__ == '__main__':
    print(isPowerOfTwo(7))
