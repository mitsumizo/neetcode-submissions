# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Section1 : 半分に分割
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        current = slow.next
        slow.next = None


        # Section2 : 後ろ側の配列を逆転
        prev = None
        while current:
            next_node = current.next # 次を退避
            current.next = prev # 次を前の要素にする
            prev = current # 次の前の要素は今の要素
            current = next_node #  currを進める

        # 各要素を交互にJoinする head と prev を交互に
        current = head
        while prev and current:
            temp_current_next = current.next
            tmp_pred_next = prev.next

            prev.next = temp_current_next
            current.next = prev
            current = prev.next
            prev = tmp_pred_next




