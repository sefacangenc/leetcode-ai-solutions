class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = 1  # Initialize the count to 1 for the root node

    def update_count(self):
        """
        Update the count attribute of the node based on the counts of its children.
        """
        self.count = 1
        if self.left:
            self.count += self.left.count
        if self.right:
            self.count += self.right.count


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Initialize a counter variable and a stack
        count = 0
        stack = []

        # Traverse the BST in-order using a stack
        while True:
            # Traverse the left subtree
            while root:
                stack.append(root)
                root = root.left

            # Check if we have visited k nodes
            if not stack:
                break
            node = stack.pop()
            count += 1
            if count == k:
                return node.val

            # Traverse the right subtree
            root = node.right


class SolutionOptimized:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Traverse the BST in-order using the count information
        while root:
            # Compute the number of nodes in the left subtree
            left_count = root.left.count if root.left else 0

            # Check if the kth smallest element is in the left subtree
            if k <= left_count:
                root = root.left
            # Check if the root node is the kth smallest element
            elif k == left_count + 1:
                return root.val
            # Check if the kth smallest element is in the right subtree
            else:
                root = root.right
                k -= left_count + 1

        # The kth smallest element was not found
        return None
