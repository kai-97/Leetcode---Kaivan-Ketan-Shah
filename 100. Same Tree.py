# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Intuition - Create traversals and compare
        def preorder(node1, values):
            if not node1:
                values.append("N")
                return
            values.append(node1.val)
            preorder(node1.left, values)
            preorder(node1.right, values)
        
        values1, values2 = [], []

        preorder(p, values1)
        preorder(q, values2)

        return values1 == values2

        ## Other solution
        # if not p and not q:
        #     return True
        # elif not p or not q:
        #     return False
        # return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)