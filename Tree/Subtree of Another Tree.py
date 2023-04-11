class Solution:
	def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
		if not t : return True
		if not s : return False

		if self.sameTree(s, t):
			return True

		return self.isSubtree(s.right, t) or self.isSubtree(s.left, t)




	def sameTree(self, s, t):
		if not s and not t :
			return True
		
		if s and t and s.val == t.val:
			return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
		
		return False
