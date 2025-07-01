# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == 0 and current.next.val is not None:
                count = 0
                inner_node = current.next

                while inner_node.val != 0:
                    count += inner_node.val
                    inner_node = inner_node.next

                current.val = count
                current.next = inner_node

            if current.next and current.next.next is None:
                current.next = None
                break

            current = current.next

        return head
