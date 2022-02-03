# 当一个字符串 s 包含的每一种字母的大写和小写形式 同时 出现在 s 中，就称这个字符串 s 是 美好 字符串。比方说，"abABB" 是美好字符串，因为 
# 'A' 和 'a' 同时出现了，且 'B' 和 'b' 也同时出现了。然而，"abA" 不是美好字符串因为 'b' 出现了，而 'B' 没有出现。 
# 
#  给你一个字符串 s ，请你返回 s 最长的 美好子字符串 。如果有多个答案，请你返回 最早 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "YazaAay"
# 输出："aAa"
# 解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
# "aAa" 是最长的美好子字符串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "Bb"
# 输出："Bb"
# 解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。 
# 
#  示例 3： 
# 
#  
# 输入：s = "c"
# 输出：""
# 解释：没有美好子字符串。 
# 
#  示例 4： 
# 
#  
# 输入：s = "dDzeE"
# 输出："dD"
# 解释："dD" 和 "eE" 都是最长美好子字符串。
# 由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 只包含大写和小写英文字母。 
#  
#  Related Topics 位运算 哈希表 字符串 滑动窗口 👍 102 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import re


class Solution:
    def __init__(self):
        # 　dfs_ok函数，把满足条件的字符串添加进来
        self.res = []

    def dfs_ok(self, Str):
        if len(Str) == 0:
            return
        # 找到哪个字符没有出现
        D = {}
        for _s in Str:
            key = _s.lower()
            D.setdefault(key, [0, 0])
            if _s.islower():
                D[key][0] = 1
            else:
                D[key][1] = 1

        try:
            not_ok_key = [d for d in D if D[d][0] * D[d][1] != 1]
        except Exception as e:
            print(e.args)
            print("error", D)
            return
        # 当前字符是完美字符，那么应该结束循环
        if len(not_ok_key) == 0:
            self.res.append(Str)
            return

        res = []
        head = 0
        for i in range(len(Str)):
            if Str[i].lower() in not_ok_key:
                rear = i
                res.append(Str[head:rear:])
                head = rear + 1
        res.append(Str[head::])
        # print("res", res)
        for r in res:
            self.dfs_ok(r)

    def longestNiceSubstring(self, s: str) -> str:
        """
        一直递归来搜索
        :param s:
        :return:
        """
        self.dfs_ok(s)
        # print(self.res)
        max_len = 0
        res = ""
        for r in self.res:
            Len = len(r)
            if Len > max_len:
                max_len = Len
                res = r
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "YazaAay"
    substring = Solution().longestNiceSubstring(s)
    print(substring)
