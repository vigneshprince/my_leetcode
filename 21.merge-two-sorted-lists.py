#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=sortedlist=ListNode()

        while list1 or list2:
            if list1 and list2:
                if list1.val<=list2.val:
                    sortedlist.next=list1
                    list1=list1.next
                else:
                    sortedlist.next=list2
                    list2=list2.next
            elif list1:
                sortedlist.next=list1
                list1=list1.next
            elif list2:
                sortedlist.next=list2
                list2=list2.next
            
            sortedlist=sortedlist.next
        return head.next


# @lc code=end

