# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        if not root:
            return None

        rhs_array = []
        next_level = [root]
        
        while next_level:
            curr_level = next_level
            next_level = []

            while curr_level:
                node = curr_level.pop(0)
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            rhs_array.append(node.val)

        return rhs_array