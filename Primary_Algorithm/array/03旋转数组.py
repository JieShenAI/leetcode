from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        n = len(nums)
        count = 0
        while True:
            count += 1
            next_index = (index + k) % n
            tmp = nums[next_index]
            nums[next_index] = nums[0]
            nums[0] = tmp
            index = next_index
            if index == 0:
                break
        if count == n:
            return
        epoch = n / count
        for i in range(1, int(epoch)):
            index = i
            while True:
                # print(nums)
                next_index = (index + k) % n
                tmp = nums[next_index]
                nums[next_index] = nums[i]
                nums[i] = tmp
                index = next_index
                if index == i:
                    break


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Solution().rotate(arr, 2)
    print(arr)
