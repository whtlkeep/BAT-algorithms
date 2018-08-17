"""
题目：
    反转字符串中的元音(vowel)字符

示例：
    Given s = "leetcode", return "leotcede".

思路：双指针
    题目很简单，直接用双指针分别从头和尾遍历字符串即可。
    当头和尾指针都遇到元音的时候，需要交换。
    注意：由于Python中字符串不允许修改，所以额外申请了一个list来存储
"""


def reverse_vowels(s):
    size = len(s)
    if size < 1:
        return s
    start = 0
    end = size - 1
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = [""] * size
    while start < end:
        if s[start] not in vowels:  # start不是元音，直接拷贝到result
            result[start] = s[start]
            start += 1
        elif s[end] not in vowels:  # end不是元音，直接拷贝到result
            result[end] = s[end]
            end -= 1
        else:  # start和end都是元音，先交换，再拷贝到result中
            result[start] = s[end]
            result[end] = s[start]
            start += 1
            end -= 1
    return "".join(result)


if __name__ == '__main__':
    print(reverse_vowels("ai"))
