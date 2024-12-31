#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        res = [''] * numRows

        currentRow = 0
        goingDown = False

        for c in s:
            res[currentRow] += c
            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown
            currentRow += 1 if goingDown else -1

        return ''.join(res)
        
# @lc code=end

