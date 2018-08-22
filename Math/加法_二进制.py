"""
题目：
    给定两个二进制字符串，返回他们的和（用二进制表示）

示例 1:
    输入: a = "11", b = "1"
    输出: "100"

示例 2:
    输入: a = "1010", b = "1011"
    输出: "10101"

思路：同其他几种"加法"
    直接按照二进制数的加法运算规则计算即可。从右到左，逐位相加，注意进位。
    下面的循环的结构是任何加法运算（二进制、字符串、链表）的通用结构，值得仔细品味
"""


def add_binary(str_a, str_b):
    end_a = len(str_a) - 1
    end_b = len(str_b) - 1
    carry = 0
    result = []
    while carry == 1 or end_a >= 0 or end_b >= 0:
        if end_a >= 0:
            carry += (ord(str_a[end_a]) - ord('0'))
            end_a -= 1
        if end_b >= 0:
            carry += (ord(str_b[end_b]) - ord('0'))
            end_b -= 1
        # 充分利用二进制数的特点，获得求和后的结果，还有进位
        result.append(str(carry % 2))
        carry = carry >> 1
    return "".join(result[::-1])


if __name__ == '__main__':
    print(add_binary("11111", "100000"))
