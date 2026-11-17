# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        node = head 
        seen = defaultdict()

        while node and node.next: 
            if node in seen:
                return True
            seen[node] = node.val
            node = node.next

        return False
        