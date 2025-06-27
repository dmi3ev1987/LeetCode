from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


sol = Solution()
test_list = [18, 6, 10, 3]
head = list_to_linkedlist(test_list)
print(linked_list_to_list(sol.insertGreatestCommonDivisors(head)))
