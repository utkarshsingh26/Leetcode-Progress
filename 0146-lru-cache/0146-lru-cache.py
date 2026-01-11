class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

        node.prev = None
        node.next = None
    
    def _add_to_front(self, node):
        toBeSecond = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = toBeSecond
        toBeSecond.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        

    def put(self, key: int, value: int) -> None:
        
        if len(self.cache) < self.capacity:
            if key in self.cache:
                toBeUpdated = self.cache[key]
                toBeUpdated.value = value
                self._remove(toBeUpdated)
                self._add_to_front(toBeUpdated)
            else:
                node = Node(key, value)
                self.cache[key] = node
                self._add_to_front(node)
        else:
            if key in self.cache:
                toBeUpdated = self.cache[key]
                toBeUpdated.value = value
                self._remove(toBeUpdated)
                self._add_to_front(toBeUpdated)
            else:
                lastNode = self.tail.prev
                self._remove(lastNode)
                del self.cache[lastNode.key]

                node = Node(key,value)
                self.cache[key] = node
                self._add_to_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)