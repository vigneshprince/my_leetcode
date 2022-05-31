#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head=1
        to_check=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=to_check:
                nums[head]=nums[i]
                head+=1
                to_check=nums[i]
        return head



        
# @lc code=end

