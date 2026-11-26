class ListNode: 
    def __init__(self, key = 0, value = 0 ,  next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next 
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_memory_mapping = defaultdict()
        
    def add_to_tail(self, node):
        prev_tail = self.tail.prev 

        prev_tail.next = node
        node.prev = prev_tail

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next 

        prev.next = next
        next.prev = prev



    def get(self, key: int) -> int:
        if key not in self.key_to_memory_mapping:
            return -1 

        curr = self.key_to_memory_mapping[key]

        self.remove(curr)

        self.add_to_tail(curr)

        return curr.value
        
        

    def put(self, key: int, value: int) -> None:

        # Case 1: Key already exists
        if key in self.key_to_memory_mapping:

            curr = self.key_to_memory_mapping[key]

            # Update its value
            curr.value = value

            # Move it to the tail
            self.remove(curr)
            self.add_to_tail(curr)

            return

        # Case 2: New key
        node = ListNode(key, value)

        self.key_to_memory_mapping[key] = node
        self.add_to_tail(node)

        # Case 3: Capacity exceeded
        if len(self.key_to_memory_mapping) > self.capacity:

            # Least recently used node is after dummy head
            lru = self.head.next

            self.remove(lru)

            del self.key_to_memory_mapping[lru.key]
        
