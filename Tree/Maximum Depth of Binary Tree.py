#Recursive DFS

"""class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0

		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


  """

#BFS

"""class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0

		level = 0

		q = deque([root])

		while q:
			for i in range(len(q)):
				node = q.popleft()
				
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			level+=1

		return level

This code is also solving the problem of finding the maximum depth of a binary tree. However, it is using the Breadth-First Search (BFS) algorithm to do so.

Here's a brief explanation of the code:

We create a queue (q) using a deque. If the root is not None, we add it to the queue.
We initialize the variable level to 0.
We enter a while loop that runs as long as the queue is not empty.
Within the while loop, we use a for loop to iterate through all the nodes at the current level of the binary tree (i.e., all the nodes currently in the queue).
For each node, we remove it from the front of the queue using q.popleft(). We then check if the node has a left child and a right child. If it does, we add both of them to the end of the queue (i.e., the back of the queue). If it has only a left child or a right child, we add that child to the back of the queue.
Once we have processed all the nodes at the current level, we increment the level variable.
After we have processed all the nodes in the binary tree, we return the value of level.
The idea behind this algorithm is to process all the nodes in the binary tree level by level. We start by adding the root node to the queue. Then, for each level, we remove all the nodes from the queue, add their children (if any) to the queue, and increment the level variable. We keep doing this until we have processed all the nodes in the binary tree.

At the end of the algorithm, the value of the level variable represents the maximum depth of the binary tree.

"""

# Iterative Depth-First Search (DFS) 

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        max_depth = 0

        if root:
            stack.append((root, 1))

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth
