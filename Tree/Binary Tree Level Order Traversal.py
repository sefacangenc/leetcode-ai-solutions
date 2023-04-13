from collections import deque  # import deque class from collections module

def levelOrder(root):
    if not root:  # If root is None, return an empty list
        return []
    
    result = []  # Initialize an empty list to store the level order traversal
    q = deque([root])  # Initialize a deque with the root node as the only element
    
    while q:  # While the deque is not empty
        level = []  # Initialize an empty list to store the nodes at the current level
        level_size = len(q)  # Get the number of nodes at the current level
        
        for i in range(level_size):  # Loop through the nodes at the current level
            node = q.popleft()  # Dequeue the node at the front of the deque
            level.append(node.val)  # Add the value of the dequeued node to the current level list
            
            # Enqueue the children of the dequeued node (if any)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        result.append(level)  # Append the current level list to the result list
    
    return result  # Return the result list containing the level order traversal
