class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == 0 and current.next.val is not None:
                count = 0
                inner_current = current.next
                
                while inner_current.val != 0:
                    count += inner_current.val
                    inner_current = inner_current.next
                
                current.val = count
                current.next = inner_current
            
            if current.next and current.next.next is None:
                current.next = None
                break

            current = current.next
        
        return head