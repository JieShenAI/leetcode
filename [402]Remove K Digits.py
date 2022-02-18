# Given string num representing a non-negative integer num, and an integer k, 
# return the smallest possible integer after removing k digits from num. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 
# which is the smallest.
#  
# 
#  Example 2: 
# 
#  
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output 
# must not contain leading zeroes.
#  
# 
#  Example 3: 
# 
#  
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with 
# nothing which is 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= num.length <= 10⁵ 
#  num consists of only digits. 
#  num does not have any leading zeros except for the zero itself. 
#  
#  Related Topics String Stack Greedy Monotonic Stack 👍 4464 👎 191

from jshen.leetcode import leetcode_test


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        总是移除第一个数和第二个数中的最大值
        :param num:
        :param k:
        :return:
        """
        l = list(num)
        for _ in range(k):
            # if len(l) > 1:
            #     if l[0] < l[1]:
            #         del l[1]
            #     else:
            #         del l[0]
            # else:
            #     return "0"
            head = l[0]
            if len(l) > 1:
                rear_idx = 1
                for idx in range(1, len(l)):
                    if l[idx] != head:
                        rear_idx = idx
                        break
                if head < l[rear_idx]:
                    del l[rear_idx]
                else:
                    del l[0]
            else:
                return '0'
        ans = str(int("".join(l)))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    func = Solution().removeKdigits
    test = leetcode_test(func)
    test.add_parameter("1219", num="1432219", k=3)
    test.add_parameter("200", num="10200", k=1)
    test.add_parameter("0", num="10", k=2)
    test.add_parameter("11", num="112", k=1)
    test.add_parameter("0", num="10", k=1)
    test.add_parameter("123", num="12345", k=2)
    test.test()
