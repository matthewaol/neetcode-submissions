# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # keep trying to traverse left
        # else just traverse right
        # stop when you reach the kth traversal

        res = root.val
        cnt = k

        def dfs(root):
            nonlocal res, cnt
            if not root:
                return

            dfs(root.left) # dive left

            cnt -= 1

            if cnt == 0:
                res = root.val
                return
            dfs(root.right)

        dfs(root)
            
        return res
