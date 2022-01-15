from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        v = 1
        for i in range(len(digits) - 1, -1, -1):
            num = v + digits[i]
            if num > 9:
                digits[i] = num % 10
                v = 1
                continue
            digits[i] = num
            v = 0
            break
        if v == 1:
            return [1] + digits
        return digits


if __name__ == '__main__':
    digits = [9, 9, 9]
    one = Solution().plusOne(digits)
    print(one)
