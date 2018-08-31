"""
题目：
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，
    使得路径上的数字总和为最小。
    说明：每次只能向下或者向右移动一步。

示例：
    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。

思路：
    最优解问题一般首选思路是动态规划!!!
    dp[i][j]是走到坐标（i,j）位置的最短路径。可以从上到下，从左到右挨个计算dp[i][j].
    由于只能向下或向右移动，那么动态转移方程是：
    dp[i][j] = max(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

    注意：本题，边界条件是最上面的一行和最左边的一列，单独处理即可！
    本题是直接在原始数组grid上修改的，没有显示的dp数组！
"""


def min_path_sum(grid):
    m = len(grid)  # m 行数
    n = len(grid[0])  # 列数
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]
    return grid[m - 1][n - 1]


if __name__ == '__main__':
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(min_path_sum(grid=grid1))
