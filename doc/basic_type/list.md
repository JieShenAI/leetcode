# 列表

## 运算

### \*

```
[1] * 3
```

> [[1, 1, 1]]



## 创建二维列表

`[[1],[1],[1]]`

创建这个列表有两种方式：

1. ```python
   a = [1]
   b = [a] * 3
   ```

   问题在于，`a` 是同一个引用，修改a[0]，b内的都会修改。

2. ```python
   b = [[1] for i in range(3)]
   ```

   发现这种方式是深复制
