# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= timePoints.length <= 2 * 10⁴ 
#  timePoints[i] 格式为 "HH:MM" 
#  
#  Related Topics 数组 数学 字符串 排序 👍 150 👎 0

from jieshen import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MOD = 24 * 60
        Min = MOD
        L = []
        for t in timePoints:
            split = t.split(':')
            L.append(int(split[0]) * 60 + int(split[1]))
        L.sort()
        for i in range(len(L) - 1):
            if L[i + 1] - L[i] < Min:
                Min = L[i + 1] - L[i]
            if Min == 0:
                return 0
        if L[0] - L[-1] + MOD < Min:
            Min = L[0] - L[-1] + MOD
        return Min


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    timePoints = ["00:00", "23:59", "00:00"]
    Min = Solution().findMinDifference(timePoints)
    print(Min)
