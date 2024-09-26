# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        stack = []

        if root:
            stack.append((root, 1))
        
        depth = 0
        while stack:
            root, current_depth = stack.pop()

            if root:
                depth = max(depth, current_depth)
                stack.append((root.left, current_depth+1))
                stack.append((root.right, current_depth+1))
        return depth
