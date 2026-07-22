class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start

    def remove_from_spot(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

        node.next = None
        node.prev = None

    def move_to_front(self, node):
        curr_first = self.start.next

        self.start.next = node
        node.prev = self.start
        curr_first.prev = node
        node.next = curr_first

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_from_spot(node)
        self.move_to_front(node)
        return node.value
    
    def remove_from_end(self):
        curr_last = self.end.prev
        curr_second_last = curr_last.prev

        curr_last.prev = None
        curr_last.next = None

        curr_second_last.next = self.end
        self.end.prev = curr_second_last

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            if key not in self.cache:
                node = Node(key, value)
                self.cache[key] = node
                self.move_to_front(node)
            else:
                node = self.cache[key]
                node.value = value
                self.remove_from_spot(node)
                self.move_to_front(node)
        else:
            if key not in self.cache:
                curr_last = self.end.prev
                key_old = curr_last.key
                del self.cache[key_old]
                self.remove_from_end()

                node = Node(key,value)
                self.cache[key] = node
                self.move_to_front(node)

            else:
                node = self.cache[key]
                node.value = value
                self.remove_from_spot(node)
                self.move_to_front(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)