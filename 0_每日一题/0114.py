import heapq
import random
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        exchange = False
        if len(nums1) > len(nums2):
            exchange = True
            nums1, nums2 = nums2, nums1
        arr = []
        ans = []
        len1 = len(nums1)
        len2 = len(nums2)
        for i in range(len1):
            heapq.heappush(arr, (nums1[i] + nums2[0], i, 0))
        while arr and len(ans) < k:

            node = heapq.heappop(arr)
            print(node)
            if exchange:
                ans.append([nums2[node[1]], nums1[node[2]]])
            else:
                ans.append([nums1[node[1]], nums2[node[2]]])
            if node[2] < len2 - 1:
                heapq.heappush(arr, (nums1[node[1]] + nums2[node[2] + 1], node[1], node[2] + 1))
            print("ans: ", ans)
        return ans


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    res = Solution().kSmallestPairs(nums1, nums2, 2)
    print(res)
