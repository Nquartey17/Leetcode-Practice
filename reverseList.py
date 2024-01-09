# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prv = None
        while current:
            nxt = current.next
            current.next = prv
            prv = current
            current = nxt
        return prv


if __name__ == '__main__':
    five = ListNode(5, None)
    four = ListNode(4, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)

    print(Solution().reverseList(one))
