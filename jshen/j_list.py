# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/2/2 10:37

"""
基础类型的扩展：list,str
"""
import random
import string
from typing import List


def list_mul(l1, l2):
    """
    列表乘法
    :param l1:
    :param l2:
    :return:
    """
    if len(l1) != len(l2):
        raise "len(l1) != len(l2)"
    products = []
    for n1, n2 in zip(l1, l2):
        products.append(n1 * n2)
    return products


def list_add(l1, l2):
    """
    列表加法
    :param l1:
    :param l2:
    :return:
    """
    products = []
    if type(l2) is not list:
        # 支持广播加法
        for n1 in l1:
            products.append(n1 + l2)
        return products

    if len(l1) != len(l2):
        raise "len(l1) != len(l2)"
    for n1, n2 in zip(l1, l2):
        products.append(n1 + n2)
    return products


def generate_random_list(bottom, top, n):
    """
    随机生成的值可以取到bottom和top
    :param bottom:
    :param top:
    :param n:
    :return:
    """
    random_list = []
    for i in range(n):
        random_list.append(random.randint(bottom, top))
    return random_list


def generate_grid(m, n, range_values=[0, 1]) -> List[List[int]]:
    """

    :param m:
    :param n:
    :param range_values: 随机生成值的范围
    :return:
    """
    assert len(range_values) == 2
    bottom = range_values[0]
    top = range_values[1]
    return [generate_random_list(bottom, top, n) for _ in range(m)]


def generate_str(n, low=True, upper=False, low_upper=False) -> str:
    """
    随机生成长度n的由26个英文字母组成的字符串
    :param n:
    :return:
    """
    if low and upper is False and low_upper is False:
        return "".join([random.choice(string.ascii_lowercase) for _ in range(n)])
    elif upper:
        return "".join([random.choice(string.ascii_uppercase) for _ in range(n)])
    else:
        return "".join([random.choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(n)])


if __name__ == '__main__':
    s = generate_str(5005)
    print(s)
