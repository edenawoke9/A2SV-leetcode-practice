# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        if head and head.next is None:
            return head
        curr=head
        next=head.next
        while next:
            if curr.val == next.val:
                curr.next=next.next
                next=next.next
            else:
                curr=next
                next=next.next
        return head
        