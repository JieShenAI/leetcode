# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i 
# - j) <= k 。如果存在，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1], k = 3
# 输出：true 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,0,1,1], k = 1
# 输出：true 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false 
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  0 <= k <= 10⁵ 
#  
#  Related Topics 数组 哈希表 滑动窗口 👍 372 👎 0
import heapq

from jieshen import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D = {}
        for i in range(len(nums)):
            key = nums[i]
            if key not in D.keys():
                D[key] = i
            else:
                if i - D[key] <= k:
                    return True
                else:
                    D[key] = i
        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1]
    k = 12
    duplicate = Solution().containsNearbyDuplicate(nums, k)
    print(duplicate)
