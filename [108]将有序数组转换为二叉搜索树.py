# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。 
# 
#  高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
# 
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 按 严格递增 顺序排列 
#  
#  Related Topics 树 二叉搜索树 数组 分治 二叉树 👍 920 👎 0

# from jieshen import *
from typing import List

from tree import *
from tree.TreeNode import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class Solution:
    def build_dfs(self, root, left, middle, right):
        # middle is index of root
        # middle = (left + right) / 2
        # index of left child: [left,middle-1]
        # index of right child: [middle + 1,right]
        if left != middle:
            left_middle = (left + middle - 1) // 2
            left_child = TreeNode(self.nums[left_middle])
            root.left = left_child
            self.build_dfs(left_child, left, left_middle, middle - 1)

        if right != middle:
            right_middle = (middle + 1 + right) // 2
            right_child = TreeNode(self.nums[right_middle])
            root.right = right_child
            self.build_dfs(right_child, middle + 1, right_middle, right)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 除2不尽，取下
        Len = len(nums)
        self.nums = nums
        self.Len = Len
        # if nums % 2 != 0:
        #     middle = Len // 2 + 1
        # else:
        middle = (0 + Len - 1) // 2
        root = TreeNode(nums[middle])
        self.build_dfs(root, 0, middle, Len - 1)
        return root


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    arr = [-10,-3,0,5,9]
    root = build_by_order(arr)
    bst = Solution().sortedArrayToBST(arr)
    print_TreeNode(bst)
