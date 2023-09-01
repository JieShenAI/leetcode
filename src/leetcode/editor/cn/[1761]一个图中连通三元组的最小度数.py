# 给你一个无向图，整数 n 表示图中节点的数目，edges 数组表示图中的边，其中 edges[i] = [ui, vi] ，表示 ui 和 vi 之间有一条
# 无向边。 
# 
#  一个 连通三元组 指的是 三个 节点组成的集合且这三个点之间 两两 有边。 
# 
#  连通三元组的度数 是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。 
# 
#  请你返回所有连通三元组中度数的 最小值 ，如果图中没有连通三元组，那么返回 -1 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# 输出：3
# 解释：只有一个三元组 [1,2,3] 。构成度数的边在上图中已被加粗。
#  
# 
#  示例 2： 
#  
#  
# 输入：n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# 输出：0
# 解释：有 3 个三元组：
# 1) [1,4,3]，度数为 0 。
# 2) [2,5,6]，度数为 2 。
# 3) [5,6,7]，度数为 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 400 
#  edges[i].length == 2 
#  1 <= edges.length <= n * (n-1) / 2 
#  1 <= ui, vi <= n 
#  ui != vi 
#  图中没有重复的边。 
#  
# 
#  Related Topics 图 👍 64 👎 0
from lib import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # 找到所有连通的3个点
        # 遍历节点
        # 遍历边，在边的两个节点的连通上，找交集，即为3个连通点
        graph = [
            [0] * (n + 1)
            for _ in range(n + 1)
        ]

        degree = [0] * (n + 1)
        for start, end in edges:
            graph[start][end] = 1
            graph[end][start] = 1
            degree[start] += 1
            degree[end] += 1

        ans = inf
        # i < j < k
        for i in range(1, n - 1):
            for j in range(i, n):
                if graph[i][j] != 1:
                    continue
                for k in range(j, n + 1):
                    if graph[i][k] == 1 and graph[j][k] == 1:
                        ans = min(
                            ans,
                            degree[i] + degree[j] + degree[k] - 6
                        )
        if ans == inf:
            return -1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
