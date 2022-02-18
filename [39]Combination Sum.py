# # Given an array of distinct integers candidates and a target integer target, 
# 
# # return a list of all unique combinations of candidates where the chosen 
# numbers 
# # sum to target. You may return the combinations in any order. 
# # 
# # The same number may be chosen from candidates an unlimited number of times. 
# 
# # Two combinations are unique if the frequency of at least one of the chosen 
# # numbers is different. 
# # 
# # It is guaranteed that the number of unique combinations that sum up to 
# # target is less than 150 combinations for the given input. 
# # 
# # 
# # Example 1: 
# # 
# # 
# # Input: candidates = [2,3,6,7], target = 7
# # Output: [[2,2,3],[7]]
# # Explanation:
# # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple 
# 
# # times.
# # 7 is a candidate, and 7 = 7.
# # These are the only two combinations.
# # 
# # 
# # Example 2: 
# # 
# # 
# # Input: candidates = [2,3,5], target = 8
# # Output: [[2,2,2,2],[2,3,3],[3,5]]
# # 
# # 
# # Example 3: 
# # 
# # 
# # Input: candidates = [2], target = 1
# # Output: []
# # 
# # 
# # 
# # Constraints: 
# # 
# # 
# # 1 <= candidates.length <= 30 
# # 1 <= candidates[i] <= 200 
# # All elements of candidates are distinct. 
# # 1 <= target <= 500 
# # 
# # Related Topics Array Backtracking 👍 9140 👎 207
# 


# leetcode submit region begin(Prohibit modification and deletion)
import copy
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.target = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.candidates.sort()
        self.target = target
        self.back_tracking(0, [0])
        return self.ans

    def back_tracking(self, sum: int, path: List[int]):
        if sum == self.target:
            self.ans.append(copy.deepcopy(path[1::]))
            return
        for c in self.candidates:
            if path[-1] > c:
                continue
            if sum + c <= self.target:
                path.append(c)
                self.back_tracking(sum + c, path)
                # 剪枝
                del path[-1]
            else:
                break

# leetcode submit region end(Prohibit modification and deletion)
