# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 队列 哈希表 字符串 计数 👍 492 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for Index in range(len(s)):
            key = s[Index]
            char_dict.setdefault(key, [0, Index])
            char_dict[key][0] += 1
        L = []
        for key in char_dict.keys():
            if char_dict[key][0] == 1:
                L.append(char_dict[key][1])
        if len(L) == 0:
            return -1
        return min(L)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().firstUniqChar("13100223")
    print(res)
