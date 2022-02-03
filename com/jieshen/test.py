# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/1/21 9:14


class stu:
    def __init__(self):
        self.name = "jshen"

    def __len__(self):
        return 1


class people:
    def __init__(self):
        pass

    def set_name(self):
        s = stu()
        return s


if __name__ == '__main__':
    # s = stu()
    # type1 = type(s)
    # print(type1)
    # print(len(s))
    p = people()
    print(type(p.set_name()))
