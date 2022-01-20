# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2]
# 输出：[2,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围是 [0, 5000] 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
# 
#  进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？ 
#  
#  
#  Related Topics 递归 链表 👍 2208 👎 0

from com.jieshen.ListNode import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # 列表存储
    def reverseList1(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        L = []
        while head is not None:
            L.append(head)
            head = head.next
        rear = L[-1]
        node = rear
        for n in L[:-1:][::-1]:
            node.next = n
            node = n
        node.next = None
        return rear

    # 递归
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is not None:
            rear = self.reverseList(head.next)
            head.next.next = head
        else:
            return head
        head.next = None
        return rear


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    head = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(head[1::][::-1])
    tree = BuildTree().build_by_array(head)
    s = Solution()
    reverse_list = s.reverseList(tree)
    print_node(reverse_list)
