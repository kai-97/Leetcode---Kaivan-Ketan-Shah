# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            size = len(queue)
            curr_level = []

            for _ in range(size):
                current_node = queue.pop(0)
                curr_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(curr_level)
        return result
    

## First solution - above solution is better complexity wise as it isnt recursion
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
    


