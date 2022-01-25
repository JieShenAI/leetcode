# 给你一个二叉树的根节点 root ， 检查它是否轴对称。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 1000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1713 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node1, node2):
        if self.check(node1, node2) is False:
            return False
        if self.check(node2, node1) is False:
            return False

    def check(self, node1, node2):
        # 两者皆None，退出
        if node1.left is None and node2.right is None:
            return
        # 一个None，一个不为None
        if node1.left is None or node2.right is None:
            return False
        # 两者皆不是None
        if node1.left.val != node2.right.val:
            return False
        # 两者相等进入递归
        elif self.dfs(node1.left, node2.right) is False:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if self.dfs(root, root) is False:
            return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = None
    b = None
    print(a == b)
