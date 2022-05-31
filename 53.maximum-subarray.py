#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums) -> int:
        maxsum=float('-inf')
        currsum=0
        for i in nums:
            if i>currsum+i:
                currsum=i
            else:
                currsum+=i
            maxsum=max(maxsum,currsum)
        return maxsum

# @lc code=end

