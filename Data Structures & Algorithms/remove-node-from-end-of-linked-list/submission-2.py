# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return_head = ListNode()
        return_head.next = head
        current = return_head
        size = 0

        while current:
            size = size + 1
            current = current.next
        
        remove_target = size - n

        current = return_head
        count = 0
        while current:
            if count + 1 == remove_target:
                current.next = current.next.next
                return return_head.next
            
            count = count + 1
            current = current.next
