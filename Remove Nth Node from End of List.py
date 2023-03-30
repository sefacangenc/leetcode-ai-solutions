"""class Solution:
	def removeNthFromEnd(self, head, ListNode,) ->  ListNode:
		dummy = ListNode(0,head)
		left = dummy
		right = head

		while n > and right:
			
			right = right.next

			n -= 1

		while right:
			left = left.next
			right = right.next

		left.next = left.next.next

		return dummy.head"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    left = right = dummy

    for i in range(n):
        right = right.next

    while right.next:
        left = left.next
        right = right.next
        
    left.next = left.next.next

    return dummy.next
