# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            lm = dfs(root.left)
            rm = dfs(root.right)
            lm = max(lm,0)
            rm = max(rm,0)
            # compute max path sum with split
            res[0] = max(res[0], root.val + lm + rm)

            return root.val + max(lm , rm)

        dfs(root)
        return res[0]