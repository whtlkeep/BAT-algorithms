"""
题目：
    给你一堆螺母和螺帽，每个螺母都有一个相对应的螺帽，但是他们之间的对应关系已经打乱。
    你可以比较螺母和螺帽的大小关系，但是你无法比较螺母和螺母的大小关系，
    你也无法比较螺帽和螺帽的大小关系。设计一个算法，找出螺母和螺帽的对应关系。

算法题：
    给两个数组nut = [A,C,E,F,B,D，...] 和bolt = [1,2,3,6,5,4,...]。其中字母A和数字1对应，B和2对应，依次内推。。。
    每个数组内部无法比较大小，数组之间可以比较大小，比如 A == 1, 1 < B, 2 > A.

思路： 快速排序，利用数组中数对另一个数组做快排
    在nut数组拿一个，可以把bolt数组分为比那个小的，比那个大的，还有一个匹配的3个部分。
    在bolt中小的那堆那一个可以把nut分成比那个小的，比那个大的，还有一个匹配的3个部分。
    这样可以发现，现在数组产生两对比配的螺母和螺钉和一队小的螺钉和螺母，一队大的螺钉和螺母。
"""


def fix(nut, bolt, left, right):
    if left >= right:
        return

    temp = nut[left]
    i = left
    j = right
    while i < j:
        while i < j and bolt[i] < temp:
            i += 1
        while i < j and bolt[j] > temp:
            j -= 1
        if i < j:
            bolt[i], bolt[j] = bolt[j], bolt[i]
    bolt[i] = temp
    bolt[left], bolt[i] = bolt[i], bolt[left]

    temp = bolt[left + 1]
    i = left + 1
    j = right
    while i < j:
        while i < j and nut[i] < temp:
            i += 1
        while i < j and nut[j] > temp:
            j -= 1
        if i < j:
            nut[i], nut[j] = nut[j], nut[i]
    nut[i] = temp
    nut[left + 1], nut[i] = nut[i], nut[left + 1]

    fix(nut, bolt, left + 2, i)
    fix(nut, bolt, i + 1, right)


if __name__ == '__main__':
    nut1 = [4, 9, 5, 1, 7, 8, 2, 3, 6]
    bolt1 = [7, 4, 1, 2, 5, 6, 9, 8, 3]
    fix(nut1, bolt1, 0, len(nut1) - 1)
    print(nut1)
    print(bolt1)
