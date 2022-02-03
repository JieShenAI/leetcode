# 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] = [
# attacki, defensei] 表示游戏中第 i 个角色的属性。 
# 
#  如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 i 弱于 存在的另一个角色 
# j ，那么 attackj > attacki 且 defensej > defensei 。 
# 
#  返回 弱角色 的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：properties = [[5,5],[6,3],[3,6]]
# 输出：0
# 解释：不存在攻击和防御都严格高于其他角色的角色。
#  
# 
#  示例 2： 
# 
#  
# 输入：properties = [[2,2],[3,3]]
# 输出：1
# 解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
#  
# 
#  示例 3： 
# 
#  
# 输入：properties = [[1,5],[10,4],[4,3]]
# 输出：1
# 解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= properties.length <= 10⁵ 
#  properties[i].length == 2 
#  1 <= attacki, defensei <= 10⁵ 
#  
#  Related Topics 栈 贪心 数组 排序 单调栈 👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numberOfWeakCharacters1(self, properties: List[List[int]]) -> int:
        """
        按照攻击值从大到小，防御值从小到大排序

        分析：
            对不同的攻击值而言：
                比它攻击值大的，已经遍历过了，而且已经记录了防御值的最大值
            对于相同的攻击值而言：
                由于在排序的时候，在攻击值相同时，防御值按照从小到大排列
                    对攻击值相同同一组而言：
                        比它防御值大的同组成员还没有遍历到，所以可以从始至终，只维持一个防御值的最大值

        :param properties:
        :return:
        """
        properties.sort(key=lambda x: (-x[0], x[1]))
        # print(properties)
        max_def = 0
        ans = 0
        for _, def_ in properties:
            if max_def > def_:
                ans += 1
            else:
                max_def = def_
        return ans

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        st = []
        ans = 0
        for attack, def_ in properties:
            while st and st[-1] < def_:
                st.pop()
                ans += 1
            st.append(def_)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    properties = [[5, 5], [6, 3], [6, 1], [6, 2], [3, 6]]
    characters = Solution().numberOfWeakCharacters(properties)
    print(characters)
    # st = []
    # st.append(1)
    # st.append(2)
    # st.append(3)
    # st.append(4)
    # pop = st.pop()
    # print(pop)
    # print(st)
