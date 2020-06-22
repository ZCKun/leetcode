from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        while (l1 is not None or l2 is not None):
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            sum = carry + x + y
            carry = int(sum / 10)
            curr.next = ListNode(sum%10)
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy_head.next


if __name__ == '__main__':
    pass