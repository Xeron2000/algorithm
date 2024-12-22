#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            maxleft1 = float('-inf') if i == 0 else nums1[i - 1]
            minright1 = float('inf') if i == m else nums1[i]
            maxleft2 = float('-inf') if j == 0 else nums2[j - 1]
            minright2 = float('inf') if j == n else nums2[j]

            if maxleft1 <= minright2 and maxleft2 <= minright1:
                if (m + n) % 2 == 0:
                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2
                else:
                    return max(maxleft1, maxleft2)
            elif maxleft1 > minright2:
                right = i - 1
            else:
                left = i + 1
        return 0

# @lc code=end

