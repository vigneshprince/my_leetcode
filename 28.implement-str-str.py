#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        check=0
        i=0
        while i < len(haystack):
            if needle[check]==haystack[i]:
                check+=1
                if check==len(needle):
                    return i-check+1
            else:
                i-=check
                check=0
            i+=1
        return -1

# @lc code=end

