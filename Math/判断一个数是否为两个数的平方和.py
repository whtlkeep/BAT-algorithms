"""
题目：
    判断一个数是否是两个数的平方和

示例：
    Input: 5
    Output: True
    Explanation: 1 * 1 + 2 * 2 = 5

思路： 双指针
    本题是要判断一个数是否等于两个数的平方和 <=等价=> 在自然数数组中，是否存在两个数的平方和是否等于一个数。
    所以本题的思路与 “/数组/Two sum - 有序数组”基本一致。

"""


def judge_square_sum(c):
    start = 0
    end = int(c ** 0.5)
    while start <= end:
        temp = start ** 2 + end ** 2
        if temp == c:
            return True
        elif temp < c:
            start += 1
        else:
            end -= 1
    return False


if __name__ == '__main__':
    print(judge_square_sum(3))
