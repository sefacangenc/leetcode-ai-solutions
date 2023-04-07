"""
Recursive Solution
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Count the number of nodes in the linked list
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        # If the number of nodes is less than k, don't reverse any nodes
        if count < k:
            return head
        
        # Reverse the first k nodes of the linked list
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Recursively call the function for the remaining linked list
        head.next = self.reverseKGroup(curr, k)
        
        # Return the new head of the modified linked list
        return prev
