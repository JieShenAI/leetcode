# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/1/23 17:30
# 参考资料: https://blog.csdn.net/weixin_39715907/article/details/109937872

"""
object.__lt__(self, other) # 小于（<）运算
object.__le__(self, other) # 小于等于（<=）运算
object.__eq__(self, other) # 等于（==）运算
object.__ne__(self, other) # 不等于（!=）运算
object.__gt__(self, other) # 大于（>）运算
object.__ge__(self, other) # 大于等于（>=）运算
"""
from random import shuffle


class Apple:
    def __init__(self, weight, code):
        self.weight = weight
        self.code = code

    def __lt__(self, other):
        """
        当weight相等的时候，code大的反而小
        :param other:
        :return:
        """
        # return self.weight < other.weight
        if self.weight < other.weight:
            return True
        elif self.weight == other.weight:
            return self.code > other.code
        return False

    # def __le__(self, other):
    #     # return self.weight <= other.weight
    #     if self.weight == other.weight:
    #         return self.code > other.code
    #     else:
    #         return self.__lt__(other)
    #
    # def __eq__(self, other):
    #     return self.weight == other.weight
    #
    # def __ne__(self, other):
    #     return self.weight != other.weight
    #
    # def __gt__(self, other):
    #     return self.weight > other.weight
    #
    # def __ge__(self, other):
    #     return self.weight >= other.weight
    #
    def __repr__(self):
        return '({},{})'.format(self.weight, self.code)


if __name__ == '__main__':
    a = Apple(1, 1)
    b = Apple(1, 2)
    c = Apple(1, 3)
    d = Apple(2, 3)
    e = Apple(3, 1)
    L = [a, b, c, d, e]
    shuffle(L)
    print(L)
    L.sort(reverse=True)
    print(L)
