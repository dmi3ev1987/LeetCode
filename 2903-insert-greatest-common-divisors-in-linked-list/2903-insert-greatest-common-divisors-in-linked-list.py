# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = head
        while current.next:
            value = current.val
            next_value = current.next.val
            max_common_divisor = 0
            for number in range(1, min(value, next_value) + 1):
                if value % number == 0 and next_value % number == 0:
                    max_common_divisor = number
            current.next = ListNode(max_common_divisor, next=current.next)
            current = current.next.next
        return head
