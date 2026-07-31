class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

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
        if len(self.cache) < self.capacity:
            if key not in self.cache:
                node = Node(key, value)
                self.move_to_front(node)
                self.cache[key] = node
            else:
                node = self.cache[key]
                node.val = value
                self.remove_from_list(node)
                self.move_to_front(node)
        else:
            if key not in self.cache:
                to_be_removed = self.end.prev
                self.remove_from_list(to_be_removed)
                del self.cache[to_be_removed.key]
                node = Node(key, value)
                self.move_to_front(node)
                self.cache[key] = node
            else:
                node = self.cache[key]
                node.val = value
                self.remove_from_list(node)
                self.move_to_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)