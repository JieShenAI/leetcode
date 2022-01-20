# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。 
# 
#  有效 二叉搜索树定义如下： 
# 
#  
#  节点的左子树只包含 小于 当前节点的数。 
#  节点的右子树只包含 大于 当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [2,1,3]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围在[1, 10⁴] 内 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 1386 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    往右走，上界不变，孩子的下界增大为自己
    往左走，下界不变，孩子的上界收缩为自己
    '''

    def check(self, head, low=None, high=None):

        # 左子树
        # 左子树节点的上界是根节点，无下界
        if head.left is not None:
            if head.left.val >= head.val:
                return False
            # 检查是否超过上界
            if high is not None and head.left.val >= high:
                return False
            # 检查是否小于下界
            if low is not None and head.left.val <= low:
                return False
            # 对左分支，执行上界收缩
            if self.check(head.left, low=low, high=head.val) is False:
                return False

        # 右子树节点的下界是根节点，上界是根节点的父节点
        if head.right is not None:
            if head.right.val <= head.val:
                return False
            # 检查是否超过上界
            if high is not None and head.right.val >= high:
                return False
            # 检查是否低于下界
            if low is not None and head.right.val <= low:
                return False
            if self.check(head.right, low=head.val, high=high) is False:
                return False

    def isValidBST(self, root: TreeNode) -> bool:
        check = self.check(root)
        if check is False:
            return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    if None is False:
        print("False")
