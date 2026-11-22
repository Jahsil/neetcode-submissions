# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      
        head = ListNode()
        ans = head
        heap = []

        for i in range(len(lists)): 
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i))
        
 
        while len(heap) > 0:
            minVal, minIndex = heapq.heappop(heap)
            head.next = lists[minIndex]
            lists[minIndex] = lists[minIndex].next
            head = head.next
            if lists[minIndex]:
                heapq.heappush(heap, (lists[minIndex].val, minIndex))

        return ans.next


