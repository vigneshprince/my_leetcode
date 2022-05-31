#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        start=0
        end=x//2
        while start<end:
            mid=(start+end)//2
            sqr=mid*mid
            if sqr==x or (sqr<x and (mid+1)*(mid+1)>x):
                return mid
            elif sqr<x:
                start=mid+1
            elif sqr>x:
                end=mid-1
        return start
# @lc code=end

