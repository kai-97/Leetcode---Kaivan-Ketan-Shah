# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node, values):
            if not node:
                return
            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)
        
        values = []
        inorder(root, values)

        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i]-values[i-1])
        return min_diff