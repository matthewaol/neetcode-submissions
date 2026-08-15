# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if there's a split
        if (p.val >= root.val and q.val <= root.val) or (p.val <= root.val and q.val >= root.val): 
            return root
        # if both values are on the right, then we traverse right
        if p.val >= root.val and q.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # if both values are on the left, then we traverse left
        if p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return None


            
        


