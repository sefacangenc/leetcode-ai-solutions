class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return self.diameter





      """               1
                       / \
                      2   3
                     / \
                    4   5
"""

"""
When we call the dfs() function on node 1, it will recursively call itself on nodes 2 and 3. Let's trace through the recursion step by step:

dfs(1) is called. Since node 1 has a left child (node 2), the function calls dfs(2).

dfs(2) is called. Since node 2 has a left child (node 4), the function calls dfs(4).

dfs(4) is called. Since node 4 has no children, the function returns a depth of 0 to its parent (dfs(2)).

dfs(5) is called. Since node 5 has no children, the function returns a depth of 0 to its parent (dfs(2)).

dfs(2) receives the depths of its left and right children (0 and 0, respectively), and returns the maximum depth plus 1 (since the current node is one level deeper than its children), which is 1. The function then returns this depth to its parent (dfs(1)).

dfs(3) is called. Since node 3 has no children, the function returns a depth of 0 to its parent (dfs(1)).

dfs(1) receives the depths of its left and right children (1 and 0, respectively), and returns the maximum depth plus 1 (since the current node is one level deeper than its children), which is 2. This is the final answer.

So the recursion proceeds as follows: dfs(1) -> dfs(2) -> dfs(4) -> return 0 to dfs(2) -> dfs(5) -> return 0 to dfs(2) -> return 1 to dfs(1) -> dfs(3) -> return 0 to dfs(1) -> return 2 to the original caller.

I hope this helps! Let me know if you have any further questions.





Call dfs(1):
- Call dfs(2):
  - Call dfs(4):
    - Return 0 (node 4 has no children)
  - Call dfs(5):
    - Return 0 (node 5 has no children)
  - Return max(0, 0) + 1 = 1 (depth of node 2)
- Call dfs(3):
  - Return 0 (node 3 has no children)
- Update diameter to max(diameter, 1 + 0) = 1 (since the path 4-2-1-3 has length 3)
- Return max(1, 0) + 1 = 2 (depth of node 1)








When dfs() is called on node 2, it first calls itself on node 4 (the left child), and then on node 5 (the right child). This is because the dfs() function starts by calling itself on the left child, and only calls itself on the right child if the left child is fully explored.

So the order of the recursive calls for this binary tree would be: dfs(1) -> dfs(2) -> dfs(4) -> dfs(5) -> dfs(3). This order ensures that we visit all nodes in the tree, since we first explore the left subtree of each node, and then the right subtree.

I hope this clarifies things! Let me know if you have any further questions."""