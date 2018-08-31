def count_one_bit_2(x):
    """ 解法二
     时间复杂度是0(v), v是二进制数的位数
     """
    count = 0
    while x != 0:
        if x & 1 == 1:  # 二进制数z的最右边的一位是1
            count += 1
        x = x >> 1  # 右移一位
    return count


def count_one_bit_3(x):
    """ 解法三
    时间复杂度是0(M), M是1的个数
    """
    count = 0
    while x:
        x = x & (x-1)  # 此操作可以将最右边的1置为0
        count += 1
    return count


if __name__ == '__main__':
    x1 = 7
    print(count_one_bit_2(x1))
    print(count_one_bit_3(x1))
