# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。 
# 
#  一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。 
# 
#  返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 500 
#  grid[i][j] 的值为 0 或 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 94 👎 0
from typing import List
from jshen.j_list import generate_random_list


def generate_grid(m, n, range_values=[0, 1]) -> List[List[int]]:
    """

    :param m:
    :param n:
    :param range_values: 随机生成值的范围
    :return:
    """
    assert len(range_values) == 2
    bottom = range_values[0]
    top = range_values[1]
    return [generate_random_list(bottom, top, n) for _ in range(m)]


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 1 <= m, n <= 500
        m = len(grid)
        n = len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] and vis[x][y] is False:
                vis[x][y] = True
                grid[x][y] = 0
                for x_d, y_d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    dfs(x + x_d, y + y_d)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        ans = 0
        for m_idx in range(m):
            for n_idx in range(n):
                if grid[m_idx][n_idx]:
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    grid = generate_grid(100, 100)
    print(grid)
    enclaves = Solution().numEnclaves(grid)
    print(enclaves)
