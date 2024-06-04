#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        if not root:
            return None
 

        if target < root.val:
            d = self.closestValue(root.left, target)
        else:
            d = self.closestValue(root.right, target)

        if d is None:
            return root.val

        err_root, err_child = abs(root.val - target), abs(d - target)
        if err_root < err_child:
            return root.val
        elif err_root == err_child:
            # If the errors are the same, return the smaller one
            return min(root.val, d)
        else:
            return d 
# @lc code=end

