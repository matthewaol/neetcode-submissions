# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        st = collections.deque()
        st.append(root)
        res = root

        while st:
            node = st.pop()

            if not node: 
                continue

            temp = node.left
            node.left = node.right
            node.right = temp

            st.append(node.right)
            st.append(node.left)
        
        return res
