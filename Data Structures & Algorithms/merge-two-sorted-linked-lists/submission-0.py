# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        list1Ptr, list2Ptr = list1, list2

        while list1Ptr and list2Ptr:
            if list1Ptr.val <= list2Ptr.val:
                node.next = list1Ptr
                node = node.next
                list1Ptr = list1Ptr.next

            else:
                node.next = list2Ptr
                node = node.next
                list2Ptr = list2Ptr.next

        if list1Ptr:
            node.next = list1Ptr
        else:
            node.next = list2Ptr
        return head.next

            