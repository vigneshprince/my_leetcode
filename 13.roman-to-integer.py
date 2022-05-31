#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sp_cases={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        num=0
        itr=0
        while itr<len(s):
            if itr+1 < len(s):
                if s[itr:itr+2] in sp_cases:
                    num+=sp_cases[s[itr:itr+2]]
                    itr+=2
                    continue
            num+=mapping[s[itr]]
            itr+=1
        return num



# @lc code=end

