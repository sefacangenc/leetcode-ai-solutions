"""class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if not root:
			return None


		#swap the children

		tmp = root.left
		root.left = root.right
		root.right = tmp

		self.invertTree(root.left)
		self.invertTree(root.right)
		return root"""
 


def invert_tree(root):
    """
    Inverts a binary tree by swapping the left and right subtrees of every node.
    """
    if root is None:
        return None

    # Recursively invert the left and right subtrees
    left_subtree = invert_tree(root.left)
    right_subtree = invert_tree(root.right)

    # Swap the left and right subtrees of the current node
    root.left = right_subtree
    root.right = left_subtree

    return root

