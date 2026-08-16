# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right): # left and right represent the bounds in which the node's value is valid
            if not node:
                return True

            if not left < node.val < right:
                return False
            
                
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float('-inf'), float('inf'))

















        #     return False

        # queue = [root]
        
        # while queue:
        #     node = queue.pop(0)

        #     if node.right and node.right.val > node.val:
        #         queue.append(node.right)
        #     if node.left and node.left.val < node.val:
        #         queue.append(node.left)
        #     if node.left and node.left.val >= node.val or node.right and node.right.val <= node.val:
        #         return False
    
        # return True