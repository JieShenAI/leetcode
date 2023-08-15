@[TOC]

## 常用类型
### list

* 删除指定元素

	```python
	.remove(item)
	```
	若列表内有多个 item，则只删除一个item



* 扩充字典

  ```python
  List.extend( arr: List )
  ```

  

### dict

* key

  必须是可 hash的，列表不可hash，列表转成元组后可hash，或字符串也可hash



* 合并

  ```python
  s1.update(s2)
  ```

  



### set
 - 初始化
	s = set()
 - 包含某个元素
	`a in s`
 - 删除某个元素

 	1. `remove(item)` 若set 不包含 item，删除会报错
 	2. `discard(item)` 若set 不包含 item，删除不报错
* 合并
	`s1.update(s2)`
* & 交集；  | 并集；



### 栈

```python
st = []

# 压栈
st.append()

# 出栈
top = st.pop()

# 栈顶
st[-1]
```



### 队列

#### queue.Queue

```python
from queue import Queue

# 加入队列
q.put(item)

# 取出队列
q.get()

# 判空
q.empty() 

# 队列个数
q.qsize()
```

特别注意，若使用`get()`取出队列时，若队列为空，会陷入死循环。

判空使用:  `q.empty() ` 不能使用 `bool(q)`， `bool(q)` 始终为 True。

队列个数： 使用 `q.qsize()`  不要使用`len(q)` 不然报错。



### 字符串

判断某个字符串是否全是数字

[2496. 数组中字符串的最大值](https://leetcode.cn/problems/maximum-value-of-a-string-in-an-array/) 

```python
is_digital = all(ch.isdigit() for ch in s)
```



## 条件

### for else & while else

当 while 循环正常执行完的情况下，执行 else 输出，如果 while 循环中执行了跳出循环的语句，比如 break ，将不执 行 else 代码块的内容。

for else 与 while else 类似

```python
v = 7
data = 4
while v >= 7:
    if data == 3:
        break
    v -= 1

else:
    print("data predict error")
```





## leetcode 常用方法

### 排序

* sorted

  ```python
  nums = sorted(enumerate(nums), key=lambda x:x[-1])
  ```

  

### 状态压缩

【注意】：<<、>>、位运算的优先级非常低，直接无脑给所有的位运算加括号。

* 全集

	```python
	(1 << n) - 1
	```
s 表示状态
x 表示选取第几个元素，从 0开始

* add or del
	```python
	def set_add_del(s, x):
		return s ^ (1 << x)
	```
* contain
	```python
	def set_contain(s, x):
		return s >> x & 1
	```

### 数组

#### 概念

* **子数组** 是数组中的一个连续部分。
* **子序列** 



#### 创建二维数组

形为 `n * m` 的二维数组 

```python
dp = [[0] * m for i in range(n)]
```



#### 棋盘方向
* 越界检测

	```python
	def check(x, y):
	    if x < 0 or x >= n or y < 0 or y >= m:
	        return False
	    return True
	```

* 8 个方向数组
	```python
	directions = [
	            (0, 1), (0, -1),
	            (1, 0), (-1, 0),
	            (1, 1), (-1, -1),
	            (-1, 1), (1, -1)
	        ]
	```
* 双重for循环
	
	```python
	for i in range(-1,2):
        for j in range(-1,2):
	        if i == 0 and j == 0:
	            continue
	```

 

###  树

#### 邻接表存储结构



```python
tree = [[] for i in range(n)]

tree = [[] for _ in range(n)]  # tree[x] 表示 x 的所有邻居/后代
for x, y in edges:
    tree[x].append(y)
    tree[y].append(x)
```



在遍历邻接表的时候，主要==无向图==的处理，避免陷入死循环。

```python
def dfs(node: int, parent: int, depth: int) -> None:
    ans[0] += depth  # depth 为 0 到 x 的距离
    for y in g[node]:  # 遍历 x 的邻居 y
        if y != parent:  # 避免访问父节点
            dfs(y, node, depth + 1)  # x 是 y 的父节点
            
```

在函数的参数添加父节点，判断后代节点不等于父节点才继续进行操作。通过此方式避免陷入死循环。



## 动态规划

### 从后往前

[392. 判断子序列](https://leetcode.cn/problems/is-subsequence/)

这一题动态规划的代码值得研读

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        if not s:
            return True
        if not t:
            return False
        """
        t_len = len(t)
        dp = [[-1] * 26 for i in range(t_len + 1)]

        get_char = lambda x: chr(ord('a') + x)
        get_ord = lambda ch: ord(ch) - ord('a')
        
        for i in range(t_len - 1, -1, -1):
            for j in range(26):
                cur_char = get_char(j)
                if t[i] == cur_char:
                    # i + 1 ?
                    dp[i][j] = i + 1
                else:
                    dp[i][j] = dp[i + 1][j]
        
        pre = 0
        for idx, ch in enumerate(s):
            if dp[pre][get_ord(ch)] == -1:
                return False
            pre = dp[pre][get_ord(ch)]
        return True
```



`dp[i][j]` 表示从`t[i]`往后遇到的第一个字母`chr(ord('a')+j)`的位置



简单理解，把dp数组视作一颗树

`dp` 形为 `(t_len + 1) x 26` ，前面要多留出一层做 根(root)

`dp[0][:]` 表示根

`dp[i][:]`  `0 < i < t_len`，只有一个值指向下层，其他值都是0。

`dp[t_len][:]` 的值全为 -1





## 排序

### 保留列表顺序

通常给某个查询(query)列表排序，进行一顿操作后，我们将处理的结果按照该query列表的顺序输出。



```
import random

n = 15
arr = [random.randint(1, 20) for item in range(15)]
print(arr)

# 将列表的顺序信息，记录在下标中
idxs = list(range(n))
# 按元素大小给小标排序
idxs.sort(key=lambda i: arr[i])
arr1 = [arr[i] for i in idxs]
print(arr1)

# 逆操作恢复
arr2 = [0] * len(arr)
for i, idx in enumerate(idxs):
    arr2[idx] = arr1[i]
print(arr2)
```

