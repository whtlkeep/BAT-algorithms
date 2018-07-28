"""
    一、题目
        求字符串中的最长回文子串。  形如 abba、aba都是
    二、思路。 动态规划
        dp[i][j]存的是string[i,...,j]是否是回文子串。是则为True, 不是则为False
    三、步骤：
        * dp初始化为False
        * if j == i, 包含一个字符的串是回文串， dp[i][j] = True
        * if j == i + 1,then:
            * if string[i] == string[j], 长度为2的两个 相同 的字符构成的子串是回文串(例如，aa,bb,cc)，True
            * if string[i] != string[j], 长度为2的两个 不同 的字符构成的子串不是回文串(例如，ac,ba,cf)，False
        * if j > i + 1, 表示子串的长度至少为3，then: （思想，如果 *** 是回文串，则 a***a 也是回文串，a***b 不是回文串）
            * if string[i] == string[j], 若dp[i+1][j-1]是回文，则dp[i][j]才是回文，否则不是
            * if string[i] != string[j], then 不是回文
"""


def longestPalindrome(string):
    size = len(string)
    dp = []
    # 初始化一个N * N的矩阵
    for i in range(size):
        row = []
        for j in range(size):
            row.append(False)
        dp.append(row)
    max_seq_len = 0
    max_seq = ""
    for i in range(size - 1, -1, -1):
        for j in range(i, size):
            if j == i:
                dp[i][j] = True
            elif j == i + 1:
                if string[i] == string[j]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                if string[i] == string[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            if j - i + 1 >= max_seq_len and dp[i][j]:
                max_seq_len = j - i + 1
                max_seq = string[i:j + 1]
    return max_seq


if __name__ == '__main__':
    string = "yyyyabcdcbawe"
    print(longestPalindrome(string))
