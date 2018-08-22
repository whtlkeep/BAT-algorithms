"""
题目：
    给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例1:
    输入:
    "tree"

    输出:
    "eert"

    解释:
    'e'出现两次，'r'和't'都只出现一次。
    因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

示例2:
    输入:
    "Aabb"

    输出:
    "bbAa"

    解释:
    此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
    注意'A'和'a'被认为是两种不同的字符。

思路:
    本题是按字符的词频对字符串进行重新排序，词频越大排在越前面。
    * 先用dict存储每个字符的频数
    * 再对dict的value项进行从大到小的顺序排序
    * 再按词频，重新组合字符串，即为结果。
"""


def frequency_sort(string):
    times = dict()
    for c in string:
        times[c] = 1 if c not in times else times[c] + 1
    times_list = sorted(times.items(), key=lambda d: d[1], reverse=True)
    result = []
    for c, t in times_list:
        result += [c] * t
    return "".join(result)


if __name__ == '__main__':
    string1 = "apple"
    print(frequency_sort(string1))
