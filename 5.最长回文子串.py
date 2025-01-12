#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        maxLength = 1
        start = 0

        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > maxLength:
                            maxLength = j - i + 1
                            start = i

        return s[start:start + maxLength]
# @lc code=end

