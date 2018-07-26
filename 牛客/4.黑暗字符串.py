# f(n) = 2*f(n-1) + f(n-2) --->  f(n)表示长度为n的字符串的黑暗字符串的个数
# 求f(n)时，可以分类考虑长度为n-1的最后两个字符相同和不相同，再讨论
# https://www.nowcoder.com/practice/7e7ccd30004347e89490fefeb2190ad2?tpId=85&tqId=29853&tPage=2&rp=2&ru=/ta/2017test&qru=/ta/2017test/question-ranking
n = int(input())
dp = [0 for i in range(31)]
dp[1] = 3
dp[2] = 9
for i in range(3, n+1):
    dp[i] = 2*dp[i-1]+dp[i-2]
print(dp[n])