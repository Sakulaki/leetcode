
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jin = 0
        l3 = ListNode(0, None)
        now = l3
        while l1 and l2:
            now.next = ListNode((l1.val + l2.val + jin) % 10, None)
            now = now.next
            jin = (l1.val + l2.val + jin) // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            now.next = ListNode((l1.val + jin) % 10, None)
            now = now.next
            jin = (l1.val + jin) // 10
            l1 = l1.next
        while l2:
            now.next = ListNode((l2.val + jin) % 10, None)
            now = now.next
            jin = (l2.val + jin) // 10
            l2 = l2.next
        if jin:
            now.next = ListNode(jin, None)
        return l3.next


