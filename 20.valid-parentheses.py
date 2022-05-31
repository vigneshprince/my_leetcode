#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mappings = {
            ")": '(',
            ']': '[',
            '}': '{'
        }
        for chr in s:
            if chr not in mappings.keys():
                stk.append(chr)
            elif stk and mappings[chr] == stk[-1]:
                stk.pop()
            else:
                return False
        return False if stk else True


# @lc code=end
