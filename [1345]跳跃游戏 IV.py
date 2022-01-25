# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。 
# 
#  每一步，你可以从下标 i 跳到下标： 
# 
#  
#  i + 1 满足：i + 1 < arr.length 
#  i - 1 满足：i - 1 >= 0 
#  j 满足：arr[i] == arr[j] 且 i != j 
#  
# 
#  请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。 
# 
#  注意：任何时候你都不能跳到数组外面。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
#  
# 
#  示例 2： 
# 
#  输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。
#  
# 
#  示例 3： 
# 
#  输入：arr = [7,6,9,6,9,6,9,7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
#  
# 
#  示例 4： 
# 
#  输入：arr = [6,1,9]
# 输出：2
#  
# 
#  示例 5： 
# 
#  输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 5 * 10^4 
#  -10^8 <= arr[i] <= 10^8 
#  
#  Related Topics 广度优先搜索 数组 哈希表 👍 89 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import queue


class node:
    def __init__(self, value, index, count=None, wait=False):
        self.value = value
        self.index = index
        self.count = count
        self.history = [value]
        self.wait = wait

    def set_wait(self, wait):
        self.wait = wait

    def new_node(self, n, count, add_history=[], wait=False):
        _node = node(value=n.value, count=self.count, index=n.index, wait=wait)
        _node.history = self.history + add_history
        _node.count += count
        return _node

    def new_add_count(self, num=0, wait=False):
        if self.count is None:
            count = num
        else:
            count = self.count + num
        return node(self.value, self.index, count, wait)

    def add_history(self, v):
        self.history.append(v)

    def __repr__(self):
        # return "value: {}, index: {}, count: {}".format(self.value, self.index, self.count)
        return repr((self.value, self.index, self.count, self.wait))


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        Len = len(arr)
        if Len == 1:
            return 0
        target = arr[-1]
        edge = {arr[0]: {}}
        edge[arr[0]].setdefault(0, [node(arr[1], 1)])
        for i in range(1, len(arr) - 1):
            # 节省空间，该节点不会被用到的
            if arr[i] == arr[i - 1] and arr[i] == arr[i + 1]:
                continue
            L = []
            if arr[i - 1] != arr[i]:
                L.append(node(arr[i - 1], i - 1))
            if arr[i + 1] != arr[i]:
                L.append(node(arr[i + 1], i + 1))
            edge.setdefault(arr[i], {})
            edge[arr[i]].setdefault(i, L)
        # print("init edge")
        # print(edge)
        q = queue.Queue()
        # 每次访问过某节点后，删除该节点
        q.put(node(arr[0], 0, 0))
        block = False
        start = True
        while q.empty() is not True:

            # print("size:", q.qsize())
            # print(q.queue)
            _node = q.get()
            # print("node: ", _node)
            if _node.wait is True:
                _node.set_wait(False)
                _node.count += 1
                q.put(_node)
                continue
            # print("sign")
            if block is True:
                if _node.count >= Min:
                    return Min

            # # 没有删除节点
            # if _node.value not in edge:
            #     continue
            # 属于自己这一族
            # 数据结构没有自己到自己的，直接加1就行。
            # 因为只有步数和同族跳转一样的，不会有更快的
            # if _node.value == target:
            #     if _node.index != Len - 1:
            #         return _node.count + 1
            #     else:
            #         return _node.count
            if _node.value == target:
                if _node.index == Len - 1:
                    return _node.count
                elif start:
                    return 1
                else:
                    block = True
                    Min = _node.count + 1
                    continue
            start = False

            # 遍历该节点可访问的节点
            for node_index in edge[_node.value].keys():
                # node_index指的是同一族，不同点连接的值
                for n in edge[_node.value][node_index]:
                    # 已经访问过，而且还不是刚刚访问的直接丢弃
                    if n.value in _node.history and _node.history[-1] != n.value:
                        continue
                    # 若是间接访问，增加等待一回合的标志
                    if _node.index != node_index:

                        # q.put(n.new_add_count(_node.count + 1, True))
                        # _node.wait = True
                        # _node.count += 1
                        # _node.index = n.index
                        # _node.value = n.value
                        # _node.history.append(n.value)
                        node_new_node = _node.new_node(n=n, count=1, wait=True, add_history=[n.value])
                        q.put(node_new_node)
                    else:
                        # node2.new_node(n=node1, count=1, wait=True, add_history=[-1])
                        new_node = _node.new_node(n=n, count=1, wait=False, add_history=[n.value])
                        q.put(new_node)
                        # q.put(n.new_add_count(_node.count + 1))
                '''
                if node_index == _node.index:
                    for n in edge[_node.value][node_index]:
                        # if n.value == target:
                        #     if n.index == Len - 1:
                        #         return _node.count + 1
                        #     # 不能return，因为有的路径可能比这快一步
                        #     else:
                        #         return _node.count + 2
                        q.put(n.new_add_count(_node.count + 1))
                    
                else:
                    for n in edge[_node.value][node_index]:
                        # if n.value == target:
                        #     if n.index == Len - 1:
                        #         return _node.count + 2
                        #     else:
                        #         return _node.count + 3
                        q.put(n.new_add_count(_node.count + 1))
                '''
            # print("删除{}".format(_node.value))
            # print("还有{}".format(edge.keys()))
            # # del edge[_node.value]
            # print(_node)
            # print(edge)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # arr = [51, 64, -15, 58, 98, 31, 48, 72, 78, -63, 92, -5, 64, -64, 51, -48, 64, 48, -76, -86, -5, -64, -86, -47, 92,
    #        -41, 58, 72, 31, 78, -15, -76, 72, -5, -97, 98, 78, -97, -41, -47, -86, -97, 78, -97, 58, -41, 72, -41, 72,
    #        -25, -76, 51, -86, -65, 78, -63, 72, -15, 48, -15, -63, -65, 31, -41, 95, 51, -47, 51, -41, -76, 58, -81,
    #        -41, 88, 58, -81, 88, 88, -47, -48, 72, -25, -86, -41, -86, -64, -15, -63]
    # --> 4

    # arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    # --> 3

    # arr = [7,7]  # 1

    arr = [6, 1, 9]
    jumps = Solution().minJumps(arr)
    print(jumps)

    # node1 = node(100, 0, 0, wait=False)
    # node1.wait = True
    # print(node1)
    # node2 = node(-100, -1, 0)
    # node2.history = [1, 2, 3]
    # new_node = node2.new_node(n=node1, count=1, wait=True, add_history=[-1])
    # print(new_node)
    # print(new_node.history)

    # n = node(100, 0)
    # n.add_count()
    # print(n)
    # n = node(100, 0)
    # print(n)
