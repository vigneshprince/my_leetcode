#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            newnum=0
            org=x
            while x>0:
                newnum=newnum*10+x%10
                x=x//10
            return newnum==org
            
        
# @lc code=end

