# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head or head.next:
        #     return

        start = head 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        
        # reverse second part of the list
        prev = None 
        secondStart = slow.next
        slow.next = None 
        secondCurr = secondStart

        while secondCurr: 
            secondNext = secondCurr.next
            secondCurr.next = prev
            prev = secondCurr
            secondCurr = secondNext


        # combine the two lists
        while prev: 
            nextNodeFirst = start.next
            nextNodeSecond = prev.next
            start.next = prev 
            prev.next = nextNodeFirst
            start = nextNodeFirst
            prev = nextNodeSecond


