# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels_dict = {}
        def traversal(node, level):
            if not node:
                return
            
            if level not in levels_dict:
                levels_dict[level] = [node.val]
            else:
                levels_dict[level].append(node.val)
            traversal(node.left, level + 1)
            traversal(node.right, level + 1)
        
        traversal(root, 1)
        return [sum(vals)/len(vals) for vals in levels_dict.values()]
