# 给你一个下标从 0 开始的二维整数数组 grid ，它的大小为 m x n ，表示一个商店中物品的分布图。数组中的整数含义为： 
# 
#  
#  0 表示无法穿越的一堵墙。 
#  1 表示可以自由通过的一个空格子。 
#  所有其他正整数表示该格子内的一样物品的价格。你可以自由经过这些格子。 
#  
# 
#  从一个格子走到上下左右相邻格子花费 1 步。 
# 
#  同时给你一个整数数组 pricing 和 start ，其中 pricing = [low, high] 且 start = [row, col] ，表示
# 你开始位置为 (row, col) ，同时你只对物品价格在 闭区间 [low, high] 之内的物品感兴趣。同时给你一个整数 k 。 
# 
#  你想知道给定范围 内 且 排名最高 的 k 件物品的 位置 。排名按照优先级从高到低的以下规则制定： 
# 
#  
#  距离：定义为从 start 到一件物品的最短路径需要的步数（较近 距离的排名更高）。 
#  价格：较低 价格的物品有更高优先级，但只考虑在给定范围之内的价格。 
#  行坐标：较小 行坐标的有更高优先级。 
#  列坐标：较小 列坐标的有更高优先级。 
#  
# 
#  请你返回给定价格内排名最高的 k 件物品的坐标，将它们按照排名排序后返回。如果给定价格内少于 k 件物品，那么请将它们的坐标 全部 返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k 
# = 3
# 输出：[[0,1],[1,1],[2,1]]
# 解释：起点为 (0,0) 。
# 价格范围为 [2,5] ，我们可以选择的物品坐标为 (0,1)，(1,1)，(2,1) 和 (2,2) 。
# 这些物品的排名为：
# - (0,1) 距离为 1
# - (1,1) 距离为 2
# - (2,1) 距离为 3
# - (2,2) 距离为 4
# 所以，给定价格范围内排名最高的 3 件物品的坐标为 (0,1)，(1,1) 和 (2,1) 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k 
# = 2
# 输出：[[2,1],[1,2]]
# 解释：起点为 (2,3) 。
# 价格范围为 [2,3] ，我们可以选择的物品坐标为 (0,1)，(1,1)，(1,2) 和 (2,1) 。
# 这些物品的排名为： 
# - (2,1) 距离为 2 ，价格为 2
# - (1,2) 距离为 2 ，价格为 3
# - (1,1) 距离为 3
# - (0,1) 距离为 4
# 所以，给定价格范围内排名最高的 2 件物品的坐标为 (2,1) 和 (1,2) 。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3
# 输出：[[2,1],[2,0]]
# 解释：起点为 (0,0) 。
# 价格范围为 [2,3] ，我们可以选择的物品坐标为 (2,0) 和 (2,1) 。
# 这些物品的排名为：
# - (2,1) 距离为 5
# - (2,0) 距离为 6
# 所以，给定价格范围内排名最高的 2 件物品的坐标为 (2,1) 和 (2,0) 。
# 注意，k = 3 但给定价格范围内只有 2 件物品。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 10⁵ 
#  1 <= m * n <= 10⁵ 
#  0 <= grid[i][j] <= 10⁵ 
#  pricing.length == 2 
#  2 <= low <= high <= 10⁵ 
#  start.length == 2 
#  0 <= row <= m - 1 
#  0 <= col <= n - 1 
#  grid[row][col] > 0 
#  1 <= k <= m * n 
#  
#  👍 5 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import queue
from typing import List


class Node:
    """
    价格：较低 价格的物品有更高优先级，但只考虑在给定范围之内的价格。
    行坐标：较小 行坐标的有更高优先级。
    列坐标：较小 列坐标的有更高优先级。
    """

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return "Node(x: {},y: {},value: {})".format(self.x, self.y, self.value)

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value > other.value:
            return False
        # 两者的value相等
        if self.x < other.x:
            return True
        if self.x > other.x:
            return False
        # 两者的行坐标也相等
        if self.y < other.y:
            return True
        return False


class Solution:

    def move(self, start):
        """
        返回合法节点的[[x,y],...]
        :param start:
        :return:
        """
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = []
        for d in direction:
            p = [start[0] + d[0], start[1] + d[1]]
            if p[0] < 0 or p[0] >= self.m or p[1] < 0 or p[1] >= self.n:
                # 越界的节点
                continue
            elif self.grid[p[0]][p[1]] == 0 or self.visited[p[0]][p[1]] == 1:
                continue
            else:
                res.append(p)
                # 记录上访问过的标志，后续不允许再次访问
                self.visited[p[0]][p[1]] = 1
        return res

    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        """
        先不考虑结构体排序
        :param grid:
        :param pricing:
        :param start:
        :param k:
        :return:
        """
        self.low = pricing[0]
        self.high = pricing[1]
        # visited数组的设立，有快速设立的方法吗？
        m = len(grid)
        self.m = m
        n = len(grid[0])
        self.n = n
        self.grid = grid
        self.visited = [[0 for j in range(n)] for i in range(m)]
        q = queue.Queue()
        q.put(start)
        self.visited[start[0]][start[1]] = 1
        res = []
        if self.low <= self.grid[start[0]][start[1]] <= self.high:
            res.append([start[0], start[1]])
        while q.empty() is False:
            Size = q.qsize()
            n = []
            while Size > 0:
                pos = q.get()
                # 对处于同一层次的node进行排序
                # print("pos: ", pos)
                for p in self.move(pos):
                    if self.low <= self.grid[p[0]][p[1]] <= self.high:
                        n.append(Node(p[0], p[1], self.grid[p[0]][p[1]]))
                    q.put([p[0], p[1]])
                # print("n: ", n)
                Size -= 1
            n.sort()
            tmp = [[n_.x, n_.y] for n_ in n]
            res += tmp
            if len(res) >= k:
                return res[:k:]
        return res

        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]
    # pricing = [2, 5]
    # start = [0, 0]
    # k = 3
    # grid = [[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]]
    # pricing = [2, 3]
    # start = [2, 3]
    # k = 2
    # grid = [[1, 1, 1], [0, 0, 1], [2, 3, 4]]
    # pricing = [2, 3]
    # start = [0, 0]
    # k = 3
    # grid = [[0, 2, 0]]
    # pricing = [2, 2]
    # start = [0, 1]
    # k = 1

    grid = [[1, 0, 1], [3, 5, 2], [1, 0, 1]]
    pricing = [2, 5]
    start = [1, 1]
    k = 9
    k_items = Solution().highestRankedKItems(grid, pricing, start, k)
    print(k_items)
