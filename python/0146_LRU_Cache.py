class Node:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.tail = self.dummy
        self.key_to_prev = {}        

    def get(self, key: int) -> int:
        if key in self.key_to_prev:
            self.move_to_end(key)
            return self.tail.value
        
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_prev: # update
            self.move_to_end(key)
            self.tail.value = value
            return
        
        self.push_back(Node(key, value)) # add

        if len(self.key_to_prev) > self.capacity:
            self.pop_front()
    
    def move_to_end(self, key):
        prev = self.key_to_prev[key]
        key_node = prev.next

        if key_node == self.tail: # already at end
            return
        
        prev.next = key_node.next
        self.key_to_prev[key_node.next.key] = prev
        key_node.next = None

        self.push_back(key_node)
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy    
