"""
题目:
    字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，
    同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

示例:
    输入: S = "ababcbacadefegdehijhklij"
    输出形式1: [9,7,8]
    输出形式2: ["ababcbaca", "defegde", "hijhklij"]

    解释:
    划分结果为 "ababcbaca", "defegde", "hijhklij"。
    每个字母最多出现在一个片段中。
    像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

思路:
    本题是想将字符串分割成若干连续的子串，使得各连续子串的字符都不相同。
    可以想到，某一具体的字符只可能出现在一个子串中。形如"a***********a"的字符串就只能划分为其本身一个子串
    启发得到，字符在字符串中的起始位置是很重要的信息，可以想象成一个闭区间。
        * 同一个子串内，不同字符的区间存在交集
        * 不同子串之间，字符的区间不存在交集

    示例讲解：
    index 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    char  a b a b c b a c a d e  f  e  g  d  e  h  i  j  h  k  l  i  j
    ****先统计每个字符的起始位置,然后按字符出现的顺序排列，如下：
    *以下区间若有交集，才并在一起；否则，不并在一起
    a -- [0, 8]
    b -- [1, 5]  ^^^^  a 并 b, get[0,8]
    c -- [4, 7]  ^^^^  [0,8] 并 c, get[0,8]
    **[0,8]与d不存在交集，说明[0,8]便是一个符合要求的子串区间
    d -- [9,14]
    e -- [10.15] ^^^^  d 并 e, get [9,15]
    f -- [11,11] ^^^^  [9,15] 并 f，get [9,15]
    g -- [13,13] ^^^^  [9,15] 并 g, get [9,15]
     **[9,15]与h不存在交集，说明[9,15]便是一个符合要求的子串区间
     同理，继续操作，即可以得到剩余的子串区间
    h -- [16,19]
    i -- [17,22]
    j -- [18,23]
    k -- [20,20]
    l -- [21,21]

"""


#  返回具体的子串
def partition_labels_return_sub_str(string):
    order = []
    start_end = dict()  # 统计每个字符的起始位置
    for i, c in enumerate(string):
        if c not in order:
            order.append(c)
            start_end[c] = [i, i]
        else:
            start_end[c][-1] = i
    result = list()
    temp = start_end[order[0]]
    for k in order[1:]:
        aft_se = start_end[k]
        if aft_se[0] > temp[1]:
            result.append(string[temp[0]:temp[1] + 1])
            temp = aft_se
        else:
            temp[1] = max(temp[1], aft_se[1])
    result.append(string[temp[0]:temp[1] + 1])
    return result


#  返回子串的长度
def partition_labels_return_len(string):
    order = []
    start_end = dict()  # 统计每个字符的起始位置
    for i, c in enumerate(string):
        if c not in order:
            order.append(c)
            start_end[c] = [i, i]
        else:
            start_end[c][-1] = i
    result = list()
    temp = start_end[order[0]]
    for k in order[1:]:
        aft_se = start_end[k]
        if aft_se[0] > temp[1]:
            result.append(temp[1] - temp[0] + 1)
            temp = aft_se
        else:
            temp[1] = max(temp[1], aft_se[1])
    result.append(temp[1] - temp[0] + 1)
    return result


if __name__ == '__main__':
    print(partition_labels_return_sub_str("ababcbacadefegdehijhklij"))
    print(partition_labels_return_len("ababcbacadefegdehijhklij"))

