# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
#  Related Topics 字符串 👍 1973 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = min([len(_) for _ in strs])
        if n == 0:
            return ""
        for i in range(n):
            block = False
            for j in strs:
                if block is False:
                    current = j[i]
                    block = True
                    continue
                if j[i] != current:
                    if i == 0:
                        return ""
                    return j[:i:]
        return j[:n:]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    strs = ["f", "", ""]
    prefix = Solution().longestCommonPrefix(strs)
    print(prefix)
