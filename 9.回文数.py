#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(int(x))[::-1] == str(x):
            return True
        else:
            return False
        
# @lc code=end

