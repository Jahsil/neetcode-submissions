# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        mxDepth = 0 

        def dfs(root, curr):
            nonlocal mxDepth

            if not root:
                return 

            dfs(root.left, curr + 1)
            dfs(root.right, curr + 1)

            mxDepth = max(mxDepth, curr)

        dfs(root, 0 )
        return mxDepth + 1

