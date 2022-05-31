#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums, val: int) -> int:
        i=0
        head=0
        while i<len(nums):
            if nums[head]==val:
                while i<len(nums)-1 and nums[i]==val:
                    i+=1
            print(i)
            if nums[i]!=val:
                nums[head]=nums[i]
                head+=1
            i+=1
        return head


# @lc code=end

