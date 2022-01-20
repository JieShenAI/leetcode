# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  输入：n = 7
# 输出：21
#  
# 
#  示例 3： 
# 
#  输入：n = 0
# 输出：1 
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
# 
#  注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/ 
# 
#  
#  Related Topics 记忆化搜索 数学 动态规划 👍 237 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
MOD = 1000000007


class Solution:
    def numWays(self, n: int) -> int:
        # 多给了一个空间，为了当n=0，程序不会发生数组越界
        dp = [0 for i in range(n + 2)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        return dp[n]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    ways = Solution().numWays(2)
    print(ways)
