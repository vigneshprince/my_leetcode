#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        start=0
        end=len(nums)
        while start<end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1 
                if nums[end]<target:
                    return mid                  
            else:
                start=mid+1
                if start<end and nums[start]>target:
                    return start
        return start

        
# @lc code=end

