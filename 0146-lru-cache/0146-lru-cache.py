class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self._remove_from_place(node)
            self._add_to_front(node)
            return node.value

    def _remove_from_place(self, node:Node):
        behind_this_node = node.prev
        ahead_this_node = node.next
        node.prev = None
        node.next = None
        behind_this_node.next = ahead_this_node
        ahead_this_node.prev = behind_this_node

    def _add_to_front(self, node: Node):
        nxt = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = nxt
        nxt.prev = node
    
    def _remove_from_back(self):
        concerned_node = self.tail.prev
        node_behind_concerned_node = concerned_node.prev

        concerned_node.prev = None
        concerned_node.next = None

        node_behind_concerned_node.next = self.tail
        self.tail.prev = node_behind_concerned_node

        return concerned_node.key 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_from_place(node)
            self._add_to_front(node)
        else:
            node = Node(key, value)

            if len(self.cache) < self.capacity:
                self.cache[key] = node
                self._add_to_front(node)
            else:
                key_to_be_evicted = self._remove_from_back()
                del self.cache[key_to_be_evicted]
                # self.cache.remove(key_to_be_evicted)
                self.cache[key] = node
                self._add_to_front(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)