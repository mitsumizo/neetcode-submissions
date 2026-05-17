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

        fast = return_head
        slow = return_head

        count = 0
        while count < n:
            fast = fast.next
            count += 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return return_head.next
        
