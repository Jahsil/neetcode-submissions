"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        if head == None: 
            return None

        translations = defaultdict()
        curr, secondCurr = head, head
        while curr: 
            newNode = Node(curr.val)
            translations[curr] = newNode
            curr = curr.next

        while secondCurr : 
           
            if secondCurr.next != None:  
                translations[secondCurr].next = translations[secondCurr.next]
            if secondCurr.random != None:
                translations[secondCurr].random = translations[secondCurr.random]
            secondCurr = secondCurr.next
            

        return translations[head]






        