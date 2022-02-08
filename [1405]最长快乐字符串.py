# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。 
# 
#  给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s： 
# 
#  
#  s 是一个尽可能长的快乐字符串。 
#  s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。 
#  s 中只含有 'a'、'b' 、'c' 三种字母。 
#  
# 
#  如果不存在这样的字符串 s ，请返回一个空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
#  
# 
#  示例 2： 
# 
#  输入：a = 2, b = 2, c = 1
# 输出："aabbc"
#  
# 
#  示例 3： 
# 
#  输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= a, b, c <= 100 
#  a + b + c > 0 
#  
#  Related Topics 贪心 字符串 堆（优先队列） 👍 90 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class s_num:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def __lt__(self, other):
        if isinstance(other, int):
            return self.n < other
        return self.n < other.n

    def __gt__(self, other):
        if isinstance(other, int):
            return self.n > other
        return self.n > other.n

    def __eq__(self, other):
        if isinstance(other, int):
            return self.n == other
        return self.n == other.n

    def sub_s(self, num=-1):
        """
        不填参数表示自动切
        :param num:
        :return:
        """
        assert num <= self.n
        # 默认参数
        if num == -1:
            if self.n == 1:
                self.n -= 1
                return self.s
            else:
                self.n -= 2
                return self.s * 2
        # 手动参数
        self.n -= num
        return self.s * num

    def __len__(self):
        return self.n

    def __repr__(self):
        return "jshen.s_num({},{})".format(self.s, self.n)


class Solution:
    def __init__(self):
        self.L = []

    def refresh(self):
        self.L = [self.Max, self.Mid, self.Min]
        self.L.sort(reverse=True)
        self.Max = self.L[0]
        self.Mid = self.L[1]
        self.Min = self.L[2]
        return self.Max > 0

    def see(self):
        return "Max: {},Mid: {},Min: {}".format(self.Max, self.Mid, self.Min)

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 每次都从最多的字母中拿2个出来；若和前一个字符一样则取次多的
        """
        eg:
            9,7,2
            aab 7,6,2
        :param a:
        :param b:
        :param c:
        :return:
        """
        # 需要一种数据结构，总是把最多的放在上面,堆，优先队列

        # 　初始化
        self.Max = s_num(a, "a")
        self.Mid = s_num(b, "b")
        self.Min = s_num(c, "c")
        res = ['@']

        # 只有self.Max > 0,才能进入循环
        while self.refresh():
            # print(res)
            # print(self.see())
            # res 还是空

            # 　判断当前最大值是否和上一个字符相等

            # 若当前最大值不等于上一个字符
            if self.Max.s != res[-1][0]:
                res.append(self.Max.sub_s())
                if self.Mid > 0:
                    res.append(self.Mid.sub_s(1))
            else:
                # 填充第2的字符，只填充1个
                if self.Mid == 0:
                    if len(res) > 1:
                        if res[-2][0] == self.Max.s:
                            break
                        if len(res[-1]) == 1:
                            res.append(self.Max.s)
                    # 考虑是否能添加Max
                    if len(res) == 1:
                        if len(res[-1]) == 1:
                            res.append(self.Max.s)
                            break
                res.append(self.Mid.sub_s(1))
        return "".join(res[1::])


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = 0
    b = 0
    c = 4
    s = Solution().longestDiverseString(a, b, c)
    print(s)
