# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    max_sum = -sys.maxsize-1
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, node: TreeNode):
        if node is None:
            return 0
        left_max = max(0, self.max_gain(node.left))
        right_max = max(0, self.max_gain(node.right))
        self.max_sum = max(self.max_sum, left_max + right_max + node.val)
        return max(left_max, right_max) + node.val
