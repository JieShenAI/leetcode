# 给你一个数组 rectangles ，其中 rectangles[i] = [li, wi] 表示第 i 个矩形的长度为 li 、宽度为 wi 。 
# 
#  如果存在 k 同时满足 k <= li 和 k <= wi ，就可以将第 i 个矩形切成边长为 k 的正方形。例如，矩形 [4,6] 可以切成边长最大为 
# 4 的正方形。 
# 
#  设 maxLen 为可以从矩形数组 rectangles 切分得到的 最大正方形 的边长。 
# 
#  请你统计有多少个矩形能够切出边长为 maxLen 的正方形，并返回矩形 数目 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：rectangles = [[5,8],[3,9],[5,12],[16,5]]
# 输出：3
# 解释：能从每个矩形中切出的最大正方形边长分别是 [5,3,5,5] 。
# 最大正方形的边长为 5 ，可以由 3 个矩形切分得到。
#  
# 
#  示例 2： 
# 
#  
# 输入：rectangles = [[2,3],[3,7],[4,3],[3,7]]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= rectangles.length <= 1000 
#  rectangles[i].length == 2 
#  1 <= li, wi <= 10⁹ 
#  li != wi 
#  
#  Related Topics 数组 👍 17 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class rec:
    def __init__(self, edge):
        self.edge = edge
        self.n = 1

    def next(self, edge):
        if self.edge == edge:
            self.n += 1
        elif self.edge < edge:
            self.edge = edge
            self.n = 1

    def __repr__(self):
        return "jshen.rec(edge={},n={})".format(self.edge, self.n)

    def __lt__(self, other):
        return self.edge < other.edge

    def __eq__(self, other):
        return self.edge == other.edge


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        r = rec(min(rectangles[0][0], rectangles[0][1]))
        for i in range(1, len(rectangles)):
            # print(r)
            r.next(min(rectangles[i][0], rectangles[i][1]))
        return r.n


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # rectangles = [[2, 3], [3, 7], [4, 3], [3, 7]]
    rectangles = [[5, 8]]
    good_rectangles = Solution().countGoodRectangles(rectangles)
    print(good_rectangles)
