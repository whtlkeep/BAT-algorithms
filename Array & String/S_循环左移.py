"""
    *例如将abcdef循环左移2位得到 cdefab

    *思路：转置 （X’Y'）' = YX
    * "abcd"[::-1] = "dcba"
"""


def left_roatet_str(str1, m):
    return ((str1[0:m])[::-1] + (str1[m:])[::-1])[::-1]


if __name__ == '__main__':
    str1 = "abcdef"
    print(left_roatet_str(str1, 2))
