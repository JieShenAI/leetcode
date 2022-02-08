# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄
# 金数量；如果该单元格是空的，那么就是 0。 
# 
#  为了使收益最大化，矿工需要按以下规则来开采黄金： 
# 
#  
#  每当矿工进入一个单元，就会收集该单元格中的所有黄金。 
#  矿工每次可以从当前位置向上下左右四个方向走。 
#  每个单元格只能被开采（进入）一次。 
#  不得开采（进入）黄金数目为 0 的单元格。 
#  矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
# 输出：24
# 解释：
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# 一种收集最多黄金的路线是：9 -> 8 -> 7。
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# 输出：28
# 解释：
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# 一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[i].length <= 15 
#  0 <= grid[i][j] <= 100 
#  最多 25 个单元格中有黄金。 
#  
#  Related Topics 数组 回溯 矩阵 👍 114 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List

visited = []
m = 0
n = 0
g_grid = []


class node:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.max_value = 0;

    # def move(self):
    #     """
    #
    #     :return:
    #     """
    #     if g_grid[self.x][self.y] == 0:
    #         return []
    #     # 已经访问过就不再访问
    #     direc = ((0, 1), (0, -1), (-1, 0), (1, 0))
    #     res = []
    #     for d in direc:
    #         new_x = self.x + d[0]
    #         new_y = self.y + d[1]
    #         if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == False and g_grid[new_x][new_y] != 0:
    #             res.append(node(new_x, new_y, self.v))
    #     return res

    def dfs(self, x, y, v):
        if v > self.max_value:
            self.max_value = v

        visited[x][y] = True
        #
        direc = ((0, 1), (0, -1), (-1, 0), (1, 0))
        for d in direc:
            new_x = x + d[0]
            new_y = y + d[1]
            if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == False and g_grid[new_x][new_y] != 0:
                self.dfs(new_x, new_y, v + g_grid[new_x][new_y])
        # 在回头剪枝的时候，消除访问记录
        # 清除痕迹
        visited[x][y] = False

    def __repr__(self):
        return "jshen.node(x={},y={},v={})".format(self.x, self.y)


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        global m
        m = len(grid)
        global n
        n = len(grid[0])
        global g_grid
        g_grid = grid
        global visited
        visited = [[False for j in range(n)] for i in range(m)]
        max_value = 0
        for i in range(m):
            for j in range(n):
                head = node(i, j)
                head.dfs(i, j, grid[i][j])
                max_value = max(max_value, head.max_value)
        return max_value


# 从该点出发遍历该店可以到达的每一点
# 在加入队列的时候，记得把权值也增加进去
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [[6]]
    s = Solution()
    gold = s.getMaximumGold(nums)
    print(gold)
