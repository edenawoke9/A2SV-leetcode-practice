
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)

        ptr1=dummy
        ptr2=dummy
        
        if (head and head.next and head.next.next==None):
            head.next=None
            return head
        if (head.next==None):
            head=None
            return head
        while ptr2 and ptr2.next and ptr2.next.next:
            ptr2=ptr2.next.next
            ptr1= ptr1.next
        
        ptr1.next=ptr1.next.next
        return head