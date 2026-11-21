# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev, curr = None, head 
        slow, fast = head, head

        i = 1
        while i < n: 
            fast = fast.next 
            i += 1
        if fast.next == None: 
            slow = slow.next
            return slow

        while fast and fast.next: 
            prev = slow 
            slow = slow.next
            fast = fast.next 
        
        if prev == None: 
            return None
        prev.next = slow.next 
        return curr