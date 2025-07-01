# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:
            value = current.val
            next_value = current.next.val

            if value == 0 and next_value is not None:
                count = 0
                inner_current = current
                while inner_current.next.val != 0:
                    count += inner_current.val
                    inner_current = inner_current.next

                current.val = count + inner_current.val
                current.next = ListNode(inner_current.next.val, next=inner_current.next.next)
                
            if current.next.next is None:
                current.next = None
                break
            current = current.next
        return head