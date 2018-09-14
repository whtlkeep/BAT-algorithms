"""
题目：岛屿的个数（200）
    给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，
    并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:
    输入:                    输出:
        11110                     1
        11010
        11000
        00000

示例 2:
    输入:                   输出:
        11000                    3
        11000
        00100
        00011

思路：
    本题是要统计岛屿的个数。首先一个岛屿的定义是由相连的1组成的。
    解题思路是，对整个二维数组进行遍历，如果遇到grid[i][j]是“1”的话，则将所有与“1”直接相连和间接相连的“1”全部
    赋值为“#”（此步骤采用递归的思路，看grid[i][j]上、下、左、右的位置是否为“1”），这样便识别出了一个完整的岛屿。
    继续遍历grid，寻找下一个岛屿。这样便可以求出岛屿的个数。

题目升级：
    不仅要求出岛屿的个数，还要求出每个岛屿中“1”的个数。
    问题很简单，在上面解题思路的基础上，在每次发现岛屿的时候，统计"#"的个数，即可求出。
"""
from pprint import pprint


class Solution:
    def num_of_islands(self, grid):
        if not grid:
            return 0
        count = 0
        pprint(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
                    print("\n发现第{}个岛屿.".format(count))
                    pprint(grid)
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


if __name__ == '__main__':
    grid1 = [["1", "1", "1", "0"],
             ["1", "0", "1", "0"],
             ["0", "0", "0", "0"],
             ["1", "0", "1", "1"],
             ["1", "0", "0", "1"]]
    so = Solution()
    print("岛屿数目是 {}".format(so.num_of_islands(grid1)))
