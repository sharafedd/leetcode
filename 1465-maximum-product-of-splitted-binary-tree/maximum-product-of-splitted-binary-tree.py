# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        MOD = 10**9 + 7

        def treeSum(node):
            if not node:
                return 0
            return node.val + treeSum(node.left) + treeSum(node.right)

        # why do we need slef?
        self.total_sum = treeSum(root)
        self.best = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            sub = node.val + left + right

            self.best = max(self.best, sub * (self.total_sum - sub))

            return sub

        dfs(root)
        return self.best % MOD




        