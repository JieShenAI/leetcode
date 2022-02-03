# 给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法： 
# 
#  
#  添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。 
#  给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。 
#  
# 
#  轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。 
# 
#  实现 DetectSquares 类： 
# 
#  
#  DetectSquares() 使用空数据结构初始化对象 
#  void add(int[] point) 向数据结构添加一个新的点 point = [x, y] 
#  int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 1
# 0]]]
# 输出：
# [null, null, null, null, 1, 0, null, 2]
# 
# 解释：
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // 返回 1 。你可以选择：
#                                //   - 第一个，第二个，和第三个点
# detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
# detectSquares.add([11, 2]);    // 允许添加重复的点。
# detectSquares.count([11, 10]); // 返回 2 。你可以选择：
#                                //   - 第一个，第二个，和第三个点
#                                //   - 第一个，第三个，和第四个点
#  
# 
#  
# 
#  提示： 
# 
#  
#  point.length == 2 
#  0 <= x, y <= 1000 
#  调用 add 和 count 的 总次数 最多为 5000 
#  
#  Related Topics 设计 数组 哈希表 计数 👍 18 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class DetectSquares:

    def __init__(self):
        # 记录某行、某列的点
        self.row = {}
        self.column = {}
        self.points_num = {}
        """
        [0,a],[a,0],[-a,0],[0,-a]
        [0,a],[-a,0]
        """

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        x = point[0]
        y = point[1]
        self.row.setdefault(x, [])
        if point not in self.row[x]:
            self.row[x].append(point)
        self.column.setdefault(y, [])
        if point not in self.column[y]:
            self.column[y].append(point)
        self.points_num.setdefault(point, 0)
        self.points_num[point] += 1

    def rectangle_count(self, point1, point2):
        num = 0
        # 先两点确定一条横边，再从poin2，找纵轴方向的点，
        a = abs(point1[1] - point2[1])
        if a == 0:
            return 0
        # 纵轴
        for p in self.column[point2[1]]:
            if abs(p[0] - point2[0]) == a:
                num += self.exist_three_point(tuple(point1), tuple(point2), tuple(p))
        return num

        #

    def exist_three_point(self, point1, point2, point3):
        # 通过三点，判断第四个点是否存在
        d = point2[0] - point3[0]
        point4 = (point1[0]-d, point1[1])
        # print("已有三个点")
        # print("p1: {}".format(point1))
        # print("p2: {}".format(point2))
        # print("p3 {}".format(point3))
        # print("p4: {}".format(point4))
        # print(self.points_num)
        if point4 not in self.points_num:
            return 0
        else:
            # print("存在")
            # print("p2_num: {}".format(self.points_num[point2]))
            # print("p3_num: {}".format(self.points_num[point3]))
            # print("p4_num: {}".format(self.points_num[point4]))
            return self.points_num[point2] * self.points_num[point3] * self.points_num[point4]

    def count(self, point: List[int]) -> int:
        # 统计point。同行，的点
        # 从该点出发,遍历该行
        num = 0
        if point[0] in self.row:
            for r_point in self.row[point[0]]:
                num += self.rectangle_count(point, r_point)
        return num


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    detectSquares = DetectSquares();
    detectSquares.add([3, 10]);
    detectSquares.add([11, 2]);
    detectSquares.add([3, 2]);
    res1 = detectSquares.count([11, 10])
    print(res1)
    #     1 。你可以选择：
    #     // - 第一个，第二个，和第三个点
    res2 = detectSquares.count([14, 8])
    print(res2)
# 0
# detectSquares.add([11, 2]); // 允许添加重复的点。
# detectSquares.count([11, 10]);
