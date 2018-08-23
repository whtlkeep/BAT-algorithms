"""
给定N个整数，查找出现次数超过N/3次的所有可能的数
注：最多只能有2个
"""


def find_mode(nums):
    size = len(nums)
    m, n = 0, 0
    cm, cn = 0, 0
    for a in nums:
        if cm == 0:
            m, cm = a, 1
        elif a == m:
            cm += 1
        elif cn == 0:
            n, cn = a, 1
        elif a == n:
            cn += 1
        else:
            cm -= 1
            cn -= 1
            if cm == 0 and cn > 0:
                m = n
                cm = cn
                cn = 0
    cm, cn = 0, 0
    for a in nums:
        if a == m:
            cm += 1
        elif a == n:
            cn += 1
    result = []
    if cm > size / 3:
        result.append(m)
    if cn > size / 3:
        result.append(n)
    return result


nums1 = [1, 2, 2, 3, 2, 1, 1, 3]
print(find_mode(nums1))
