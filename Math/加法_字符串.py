"""
题目：大数相加
    给定两个字符串形式的非负整数 str_a 和 str_b ，计算它们的和。
    ！！！注意:
        str_a 和 str_b 的长度都小于 5100
        str_a 和 str_b 都只包含数字 0-9
        str_a 和 str_b 都不包含任何前导零
        你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

示例 1:
    输入: a = "979", b = "1211"
    输出: "2190"

思路：
    思路 同其他几种"加法"
    将两个数按最右端对齐，逐位相加。
    下面的循环的结构是任何加法运算（二进制、字符串、链表）的通用结构，值得仔细品味
"""


def add_string(str_a, str_b):
    end_a = len(str_a) - 1
    end_b = len(str_b) - 1
    carry = 0
    result = []
    while carry > 0 or end_a >= 0 or end_b >= 0:
        if end_a >= 0:
            carry += (ord(str_a[end_a]) - ord('0'))
            end_a -= 1
        if end_b >= 0:
            carry += (ord(str_b[end_b]) - ord('0'))
            end_b -= 1
        result.append(str(carry % 10))
        carry = int(carry / 10)
    return "".join(result[::-1])


if __name__ == '__main__':
    print(add_string("979", "1211"))
