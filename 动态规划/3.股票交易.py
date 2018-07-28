"""题目1----交易1次
给定数组A[0....N-1],其中A[i]表示某股票第i天的价格。如果允许最多只进行一次交易
(先买一次，再卖一次），请计算何时买卖达到最大收益，返回最大收益值。
结题思路：遍历prices数组，如果在第i次（1<=i<len）卖出,则必须在第j次（0<=j<i）买入，买入的值越小越好。
"""


def maxProfit1(prices):
    p = 0
    minv = prices[0]
    for i in range(1, len(prices)):
        minv = min(minv, prices[i - 1])
        p = max(p, prices[i] - minv)
    return p


"""题目2----最多交易K次
给定数组A[0...N-1]，其中A[I]表示某股票第i天的价格。如果允许 最多 只进行K次交易（先买一次再卖一次算一次交易）。
请计算何时买卖到达最大收益，返回最大收益值。
规定: 买卖不能嵌套，只能“买 卖 买 卖”
思路：使用dp.
dp[k][i]表示最多K次交易在第i天的最大收益。
在第i天，有两种选择：要么卖出股票，要么不卖出股票，从而得到状态转移方程是：
dp[k][i]=max(dp[k][i-1], dp[k-1][j] + prices[i]-prices[j]),    j in range[0,i]
              不卖出             卖出
              
dp[k][i]=max(dp[k][i-1],prices[i] + {max(dp[k-1][j]-prices[j])j in range[0,i]})
              不卖出             卖出         
"""


def maxProfit2_1(prices, K):
    dp = []
    for k in range(K + 1):
        row = []
        for i in range(len(prices)):
            row.append(0)
        dp.append(row)
    for k in range(1, K + 1):
        for i in range(1, len(prices)):
            for j in range(i):
                dp[k][i] = max(dp[k][i - 1], dp[k - 1][j] + prices[i] - prices[j])
    return dp[K][len(prices) - 1]


def maxProfit2_2(prices, K):
    # 初始化dp[k][i]
    dp = []
    for k in range(K + 1):
        row = []
        for i in range(len(prices)):
            row.append(0)
        dp.append(row)
    # 状态转移方程
    for k in range(1, K + 1):
        mx = dp[k - 1][0] - prices[0]
        for i in range(1, len(prices)):
            dp[k][i] = max(dp[k][i - 1], mx + prices[i])
            mx = max(mx, dp[k - 1][i] - prices[i])
    return dp[K][len(prices) - 1]


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit2_2(prices, 3))
