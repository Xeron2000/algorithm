#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        I , V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
        res = 0
        roman = {'I': I, 'V': V, 'X': X, 'L': L, 'C': C, 'D': D, 'M': M}
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
# @lc code=end