# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 
# 
#  
#  push(x) —— 将元素 x 推入栈中。 
#  pop() —— 删除栈顶的元素。 
#  top() —— 获取栈顶元素。 
#  getMin() —— 检索栈中的最小元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  pop、top 和 getMin 操作总是在 非空栈 上调用。 
#  
#  Related Topics 栈 设计 👍 1161 👎 0

from jshen.j_list import generate_random_list

# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class MinStack:

    def __init__(self):
        self._len = 0
        self.data = []
        self.Min = []

    def cur(self):
        return self._len - 1

    def push(self, val: int) -> None:
        # self.Min = min(self.Min[self.cur], val)
        if self._len == len(self.data):
            self.data.append(val)
        else:
            self.data[self._len] = val
        self._len += 1
        if self._len == 1:
            if len(self.Min) == 0:
                self.Min.append(val)
            else:
                self.Min[0] = val
        else:
            bottom = min(self.Min[self.cur()-1],val)
            try:
                self.Min[self.cur()] = bottom
            except:
                self.Min.append(bottom)

    def pop(self) -> None:
        """
        在出栈的时候，若出栈的是最小值，则需要更改self.Min
        :return:
        """
        self._len -= 1


    def top(self) -> int:
        return self.data[self.cur()]

    def getMin(self) -> int:
        return self.Min[self.cur()]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    """
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]
"""
    mst = MinStack()
    mst.push(-2)
    mst.push(0)
    # mst.push(-3)
    # print(mst.getMin())
    # mst.pop()
    # mst.top()
    # get_min = mst.getMin()
    # print(get_min)
