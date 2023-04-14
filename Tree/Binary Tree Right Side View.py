"""class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        
        q, res = [root], []
        
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                
                if node.left:   
                    q.append(node.left)
                
                if node.right:  
                    q.append(node.right)
            
            res.append(node.val)
        
        return res"""


"""from collections import deque

def rightSideView(root):
    if not root:
        return []

    queue = deque([root])
    right_side = []

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:
                right_side.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_side

"""




    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []  # Initialize an empty list to hold the right side view of the binary tree
        q = collections.deque([root])  # Create a deque and add the root to it

        while q:  # Start the BFS loop
            rightSide = None  # Initialize the right side variable as None
            qLen = len(q)  # Get the current size of the queue

            for i in range(qLen):  # Traverse the current level of the binary tree
                node = q.popleft()  # Get the first node in the queue and remove it
                if node:  # If the node is not None
                    rightSide = node  # Update the right side variable
                    q.append(node.left)  # Add the left child of the node to the queue
                    q.append(node.right)  # Add the right child of the node to the queue

            if rightSide:  # If the right side variable is not None, i.e., if there is a node on the right side of the current level
                res.append(rightSide.val)  # Add the value of the rightmost node to the result list

        return res  # Return the right side view of the binary tree
