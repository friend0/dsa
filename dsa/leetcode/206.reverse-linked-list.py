#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last, temp = None, None
        cur = head
        while cur:
            temp = cur.next
            if last:
                cur.next = last
            else:
                cur.next = None
                # print(last.val)
            last = cur
            if temp:
                cur = temp
            else:
                break
        return cur


# @lc code=end
