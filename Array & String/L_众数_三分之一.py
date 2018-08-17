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
        elif cn == 0:
            n, cn = a, 1
        elif a == m:
            cm += 1
        elif a == n:
            cn += 1
        else:
            cm -= 1
            cn -= 1
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


nums = [1, 2, 3, 2, 5, 2, 2, 3, 3, 2, 3]
print(find_mode(nums))
