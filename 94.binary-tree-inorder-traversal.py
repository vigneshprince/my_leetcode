#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk=[]
        ret=[]
        while True:
            if root:
                stk.append(root)
                root=root.left
            elif stk:
                root=stk.pop()
                ret.append(root.val)
                root=root.right
            else:
                break
        return ret

        
# @lc code=end

