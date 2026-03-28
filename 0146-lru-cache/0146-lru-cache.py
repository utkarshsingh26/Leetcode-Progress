class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start

        self.capacity = capacity
        self.cache = {}
    
    def _remove_from_list(self, node):
        previous_node = node.prev
        next_node = node.next

        node.prev = None
        node.next = None

        previous_node.next = next_node
        next_node.prev = previous_node
    
    def _add_to_front(self, node):
        current_top = self.start.next

        self.start.next = node
        node.prev = self.start

        node.next = current_top
        current_top.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove_from_list(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove_from_list(node)
            self._add_to_front(node)
        else:
            if len(self.cache) < self.capacity:
                node = Node(key,value)
                self.cache[key] = node
                self._add_to_front(node)
            elif len(self.cache) == self.capacity:
                last_node = self.end.prev
                self._remove_from_list(last_node)
                del self.cache[last_node.key]

                node = Node(key,value)
                self.cache[key] = node
                self._add_to_front(node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)