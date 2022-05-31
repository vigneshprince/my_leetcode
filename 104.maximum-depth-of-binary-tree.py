#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth=0
        if root:
            stk=[root]
            while stk:
                print(len(stk))
                maxdepth+=1
                for i in range(len(stk)):
                    root=stk.pop()
                    if root.left:
                        stk.append(root.left)
                    if root.right:
                        stk.append(root.right)
            return maxdepth
        return 0
        
# @lc code=end

