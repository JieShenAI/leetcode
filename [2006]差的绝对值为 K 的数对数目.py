# 给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。
#  
# 
#  |x| 的值定义为： 
# 
#  
#  如果 x >= 0 ，那么值为 x 。 
#  如果 x < 0 ，那么值为 -x 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,2,1], k = 1
# 输出：4
# 解释：差的绝对值为 1 的数对为：
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,3], k = 3
# 输出：0
# 解释：没有任何数对差的绝对值为 3 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [3,2,1,5,4], k = 2
# 输出：3
# 解释：差的绝对值为 2 的数对为：
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  1 <= k <= 99 
#  
#  Related Topics 数组 哈希表 计数 👍 16 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
from typing import List


class Solution:
    def countKDifference1(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans

    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        Q:|i-j| = k,已知j=num,求i?
        A:    i = k + j or i = -k + j
        """
        # 统计到当前index，nums[idx] = i 的个数
        cnt = Counter()
        ans = 0
        for num in nums:
            # 因为k >= 1，所以先统计cnt和后统计都可以
            # cnt[num] += 1
            ans += cnt[k + num] + cnt[-k + num]
            cnt[num] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1]
    k_difference = Solution().countKDifference(nums, 3)
    print(k_difference)
