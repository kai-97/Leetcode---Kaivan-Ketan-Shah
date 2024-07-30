# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}
        def levelOrderTraversal(node, level):
            if not node:
                return
            if level in result:
                result[level].append(node.val)
            else:
                result[level] = [node.val]
            levelOrderTraversal(node.left, level+1)
            levelOrderTraversal(node.right, level+1)
            
        levelOrderTraversal(root, 0)
        return result.values()