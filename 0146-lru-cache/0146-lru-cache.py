class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.start = Node(0,0)
        self.end = Node(0,0)

        self.start.next = self.end
        self.end.prev = self.start
    
    def remove_from_list(self, node):
        before = node.prev
        after = node.next

        node.next = None
        node.prev = None
        before.next = after
        after.prev = before
    
    def move_to_front(self, node):
        curr_first = self.start.next

        self.start.next = node
        node.prev = self.start

        node.next = curr_first
        curr_first.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_from_list(node)
        self.move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]
            self.remove_from_list(node)
            self.move_to_front(node)
            return

        if len(self.cache) < self.capacity:
            node = Node(key, value)
            self.move_to_front(node)
            self.cache[key] = node
        else:
            curr_last = self.end.prev
            del self.cache[curr_last.key]
            self.remove_from_list(curr_last)

            node = Node(key, value)
            self.move_to_front(node)
            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)