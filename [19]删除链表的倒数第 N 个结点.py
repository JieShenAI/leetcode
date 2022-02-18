# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1], n = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2], n = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中结点的数目为 sz 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
# 
#  进阶：你能尝试使用一趟扫描实现吗？ 
#  Related Topics 链表 双指针 👍 1755 👎 0

# Definition for singly-linked list.


from jieshen.ListNode import BuildTree, ListNode, print_node


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        L = []
        while head is not None:
            L.append(head)
            head = head.next
        L.append(None)
        Len = len(L) - 1
        print("len: ", Len)
        print("index: ", Len - n - 1)
        if Len - n - 1 < 0:
            return L[Len - n + 1]
        first = L[Len - n - 1]
        first.next = first.next.next
        return L[0]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    head = BuildTree(arr).build_by_array()
    tree = Solution().removeNthFromEnd(head, 1)
    print_node(tree)
