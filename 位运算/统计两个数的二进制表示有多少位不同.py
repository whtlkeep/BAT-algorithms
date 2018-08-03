"""
一、题目
    统计两个数的二进制表示有多少位不同，即汉明距离

二、示例
    输入: x = 1, y = 4
    输出: 2
    解释:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

    上面的箭头指出了对应二进制位不同的位置。

三、思路
    有上面的解释过程可以想到要统计不同的字符数，进行异或操作即可,
    对于二进制数，只有 1^ 0 = 1, 正好可以统计不同点
    1^4 = (0 1 0 1)  count = 2
"""


def hammingDistance(x, y):
    z = x ^ y
    count = 0
    # 接下来统计二进制数z中1的个数
    while z != 0:
        if z & 1 == 1:  # 二进制数z的最右边的一位是1
            count += 1
        z = z >> 1  # 右移一位
    return count


if __name__ == '__main__':
    print(hammingDistance(1, 4))
