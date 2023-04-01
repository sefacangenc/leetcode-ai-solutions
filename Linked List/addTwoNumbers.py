"""class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1, l2):
		dummy = ListNode()
		cur = dummy

		carry = 0

		while l1 or l2 or carry:
			v1 = l1.val if l1 else 0
			v2 = l2.val if l2 else 0

			#new digit 
			val = v1 + v2 + carry
			carry = val // 10 
			val = val % 10 
			cur.next = ListNode(val)


			#update pointers
			cur = cur.next
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None

		return dummy.next"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0) # create a dummy node
    curr = dummy # set current node to dummy node
    carry = 0 # initialize carry to 0
    
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0 # set v1 to the value of the current node in l1 or 0 if l1 is None
        v2 = l2.val if l2 else 0 # set v2 to the value of the current node in l2 or 0 if l2 is None
        val = v1 + v2 + carry # calculate the sum of v1, v2, and carry
        
        carry = val // 10 # calculate the carry by dividing the sum by 10
        val = val % 10 # calculate the value to be added to the new node by taking modulo 10
        
        curr.next = ListNode(val) # create a new node with the calculated value and add it to the current node's next
        curr = curr.next # move the current node to the newly created node
        
        l1 = l1.next if l1 else None # move l1 to the next node if it exists, otherwise set it to None
        l2 = l2.next if l2 else None # move l2 to the next node if it exists, otherwise set it to None
    
    return dummy.next # return the next node after the dummy node, which is the start of the new linked list
