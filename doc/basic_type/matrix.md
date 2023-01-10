# 得到col : List[List[int]]
matrix: List[List[int]]
```python
cols = list(zip(*matrix))
```
\*是解包，即拿掉列表里面的每个子列表。zip把每个子列表对应的元素抽出来组成新列表；

# row min
matrix元素各不一样
```python
for rows in matrix:
    num = min(rows)
    c = rows.index(num)
```
得到每一行的最小值和对应的index
