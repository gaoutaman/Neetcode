# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative
# T O(n), M O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


# Recursive
# T O(n), M O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case, if head is null,return null
        if not head:
            return None

        newHead = head
        # if head.next is not null
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
