#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for itr,num in enumerate(nums):
            if num in check:
                return [check[num],itr]
            else:
                check[target-num]=itr
# @lc code=end

