#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p or q:
            pdeq=deque([p])
            qdeq=deque([q])
            flag=True
            while True:
                if pdeq or qdeq:
                    p=pdeq.popleft()
                    q=qdeq.popleft()
                    if p and q and p.val==q.val:
                        if p.left:
                            flag=not flag
                            pdeq.append(p.left)
                        if q.left:
                            flag=not flag
                            qdeq.append(q.left)
                        if not flag:
                            return False
                        if p.right:
                            flag=not flag
                            pdeq.append(p.right)
                        if q.right:
                            flag=not flag
                            qdeq.append(q.right)
                        if not flag:
                            return False
                    else:
                        return False
                else:
                    return True
        else:
            return True


# @lc code=end

