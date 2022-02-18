# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。 
# 
#  从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。 
# 
#  返回可能的 最小差值 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [90], k = 1
# 输出：0
# 解释：选出 1 名学生的分数，仅有 1 种方法：
# - [90] 最高分和最低分之间的差值是 90 - 90 = 0
# 可能的最小差值是 0
#  
# 
#  示例 2： 
# 
#  输入：nums = [9,4,1,7], k = 2
# 输出：2
# 解释：选出 2 名学生的分数，有 6 种方法：
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 1 = 8
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 7 = 2
# - [9,4,1,7] 最高分和最低分之间的差值是 4 - 1 = 3
# - [9,4,1,7] 最高分和最低分之间的差值是 7 - 4 = 3
# - [9,4,1,7] 最高分和最低分之间的差值是 7 - 1 = 6
# 可能的最小差值是 2 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 1000 
#  0 <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 排序 滑动窗口 👍 27 👎 0

from jshen import j_list

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        step = k - 1
        Min = 10 ** 5 + 1
        for idx in range(k - 1, len(nums)):
            Min = min(nums[idx] - nums[idx - step], Min)
        return Min


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [90]
    k = 1
    difference = Solution().minimumDifference(nums, k)
    print(difference)
    random_list = j_list.generate_random_list(0, 10 ** 5, 1000)
    print(random_list)
