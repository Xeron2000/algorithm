#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)        
            else:
                if stack and char == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack
        
# @lc code=end

