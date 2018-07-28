# coding:utf-8
"""
有一个容量为 N 的背包，要用这个背包装下物品的价值最大，这些物品有两个属性：体积 w 和价值 v。

定义一个二维数组 dp 存储最大价值，其中 dp[i][j] 表示前 i 件物品体积不超过 j 的情况下能达到的最大价值。
设第 i 件物品体积为 w，价值为 v，根据第 i 件物品是否添加到背包中，可以分两种情况讨论：

    第 i 件物品没添加到背包，总体积不超过 j 的前 i 件物品的最大价值就是总体积不超过 j 的前 i-1 件物品的最大价值，dp[i][j] = dp[i-1][j]。
    第 i 件物品添加到背包中，dp[i][j] = dp[i-1][j-w] + v。

第 i 件物品可添加也可以不添加，取决于哪种情况下最大价值更大。

综上，0-1 背包的状态转移方程为：
    dp[i][j] = max( dp[i-1][j], dp[i-1][j-w] + v )
"""
# def knapsack(W, N, weights, values):
#     dp = []
#     for i in range(N + 1):
#         row = []
#         for j in range(W + 1):
#             row.append(0)
#         dp.append(row)
#     for i in range(1, N+1):
#         w = weights[i-1]
#         v = values[i-1]
#         for j in range(1, W+1):
#             if j >= w:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
#             else:
#                 dp[i][j] = dp[i-1][j]
