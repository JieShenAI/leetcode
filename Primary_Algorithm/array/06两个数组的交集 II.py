from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        s1_index = 0
        s2_index = 0
        s1_len = len(nums1)
        s2_len = len(nums2)
        res = []
        while s1_index < s1_len and s2_index < s2_len:
            if nums1[s1_index] == nums2[s2_index]:
                res.append(nums1[s1_index])
                s1_index += 1
                s2_index += 1
                continue
            if nums1[s1_index] < nums2[s2_index]:
                s1_index += 1
                continue
            s2_index += 1
        return res


if __name__ == '__main__':
    nums1 = [4]
    nums2 = [9]
    intersect = Solution().intersect(nums1, nums2)
    print(intersect)
