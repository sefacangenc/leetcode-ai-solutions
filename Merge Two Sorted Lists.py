class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to serve as the head of the merged list
        dummy = ListNode(-1)
        # create a pointer to traverse the merged list
        current = dummy
        
        # traverse both lists while they are not empty
        while list1 and list2:
            # compare the values of the current nodes of both lists
            if list1.val <= list2.val:
                # append the node from list1 to the merged list
                current.next = list1
                # move the pointer to the next node of list1
                list1 = list1.next
            else:
                # append the node from list2 to the merged list
                current.next = list2
                # move the pointer to the next node of list2
                list2 = list2.next
            # move the pointer of the merged list to the last appended node
            current = current.next
        
        # append the remaining nodes of list1 or list2, if any
        current.next = list1 if list1 else list2
        
        # return the head of the merged list (excluding the dummy node)
        return dummy.next
