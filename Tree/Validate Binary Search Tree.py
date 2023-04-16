class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not dfs(node.left, lower, node.val):
                return False
            if not dfs(node.right, node.val, upper):
                return False
            return True

        return dfs(root)
