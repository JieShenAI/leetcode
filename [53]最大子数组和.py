# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  子数组 是数组中的一个连续部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
#  Related Topics 数组 分治 动态规划 👍 4297 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left_sum = 0
        max_sum = nums[0]
        for n in nums:
            # 当前数 + 左边和 > 0，更新left_num
            tmp = left_sum + n
            if tmp > max_sum:
                max_sum = tmp
            if tmp < 0:
                left_sum = 0
            else:
                left_sum = tmp
            # print(max_sum)
        return max_sum


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [5, 4, -1, 7, 8]
    array = Solution().maxSubArray(nums)
    print(array)
