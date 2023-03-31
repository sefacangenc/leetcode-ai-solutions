"""class Solution:
	def copyRandomList(self, head):

		oldToCopy = {None : None}

		cur = head

		while cur:
			copy = Node(cur.val)
			oldToCopy[cur] = copy

			cur = cur.next


		cur = head

		while cur:
			copy = oldToCopy[cur] 
			copy.next = oldToCopy[cur.next]
			copy.random = oldToCopy[cur.random]
			cur = cur.next

		return oldToCopy[head] 


"""

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
        
def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None
    
    oldToCopy = {}
    cur = head
    
    # Create new nodes for each original node and store them in a dictionary
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next
    
    # Set the next and random pointers of the new nodes using the dictionary
    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy.get(cur.next)
        copy.random = oldToCopy.get(cur.random)
        cur = cur.next
    
    # Return the head of the new list
    return oldToCopy[head]
