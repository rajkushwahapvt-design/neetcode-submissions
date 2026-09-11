# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next=None
        prev=None
        nxt=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        left=head
        right=prev
        while left and right:
            temp1=left.next
            temp2=right.next
            left.next=right
            right.next=temp1
            left=temp1
            right=temp2
        