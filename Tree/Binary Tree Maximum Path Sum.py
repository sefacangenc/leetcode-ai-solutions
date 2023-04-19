class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.helper(root)
        return self.max_sum
    
    def helper(self, node):
        if not node:
            return 0
        
        left_sum = max(0, self.helper(node.left))
        right_sum = max(0, self.helper(node.right))
        
        current_sum = left_sum + right_sum + node.val
        self.max_sum = max(self.max_sum, current_sum)
        
        return max(left_sum, right_sum) + node.val
