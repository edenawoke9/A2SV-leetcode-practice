from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
      
        if fast:  
            slow = slow.next
        
       
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        
        return True
