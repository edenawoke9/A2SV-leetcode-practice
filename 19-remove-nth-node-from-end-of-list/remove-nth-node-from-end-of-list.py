from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        aheadptr = dummy
        travptr = dummy
        count = 0

        while aheadptr.next is not None:
            aheadptr = aheadptr.next
            count += 1
            if count > n:
                travptr = travptr.next

        travptr.next = travptr.next.next  
        return dummy.next  
