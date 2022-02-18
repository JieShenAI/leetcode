# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/2/18 10:04

class leetcode_test():
    def __init__(self, func):
        self.func = func
        self.data_set = []

    def add_parameter(self, result, **kwargs):
        self.data_set.append((result, kwargs))

    def test(self):
        for (result, kwargs) in self.data_set:
            ans = self.func(**kwargs)
            if result == ans:
                continue
            else:
                print(f"error: input: {kwargs}")
                print(f"expect: {result}, but get: {ans}")


if __name__ == '__main__':
    pass
