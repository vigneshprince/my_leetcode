#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret=''
        for itr,i in enumerate(min(strs, key=len)):
            if all([i == x[itr] for x in strs]):
                ret+=i
            else:
                break
        return ret
# @lc code=end

