#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        stack = []
        if x < 0:
            stack.append('-')
            x = abs(x)
        while x > 0:
            stack.append(x % 10)
            x = x // 10
        res = 0
        while stack:
            res = res * 10 + stack.pop()
        if res > 2**31 - 1 or res < -2**31:
            return 0
        return res
# @lc code=end

