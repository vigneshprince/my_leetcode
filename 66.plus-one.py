#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        digits[i]+=1
        while digits[i]==10:
            digits[i]=0
            i-=1
            if i>=0:
                digits[i]+=1
            else:
                return [1]+digits
        return digits
        
# @lc code=end

