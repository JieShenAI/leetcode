# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [], l2 = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两个链表的节点数目范围是 [0, 50] 
#  -100 <= Node.val <= 100 
#  l1 和 l2 均按 非递减顺序 排列 
#  
#  Related Topics 递归 链表 👍 2144 👎 0

from jieshen import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def print_node(head: ListNode):
    print("node:", end="")
    if head is None:
        print(None)
        return
    while head is not None:
        print(head.val, end=",")
        head = head.next
    print()

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)
        head_bak = head

        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None:
                print_node(head_bak)
                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
                # head.next = None
                print("after")
                print_node(head_bak)
                continue

            if list1 is None:
                # list2必不空
                print("list1 is None")
                head.next = list2
                head = head.next
                list2 = list2.next
                head.next = None
            else:
                print("list2 is None")
                head.next = list1
                head = head.next
                list1 = list1.next
                head.next = None
        head.next = None
        return head_bak.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    List1 = []
    List2 = []
    tree1 = BuildTree().build_by_array(List1)
    tree2 = BuildTree().build_by_array(List2)
    lists = Solution().mergeTwoLists(tree1, tree2)
    print_node(lists)
    # List2 = List1
    # List1[0] = 100
    # print(List2)
