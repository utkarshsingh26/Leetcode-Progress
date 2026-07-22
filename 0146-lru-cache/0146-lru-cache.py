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

    def remove_from_list(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

        node.prev = None
        node.next = None
    
    def add_to_top(self, node):
        curr_top = self.start.next

        self.start.next = node
        node.prev = self.start
        node.next = curr_top
        curr_top.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_from_list(node)
        self.add_to_top(node)
        return node.value
    
    def take_out_last(self):
        curr_last = self.end.prev
        new_last = curr_last.prev

        new_last.next = self.end
        self.end.prev = new_last

        curr_last.next = None
        curr_last.prev = None

        return curr_last.key


    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            if key not in self.cache:
                node = Node(key,value)
                self.cache[key] = node
                self.add_to_top(node)
            else:
                node = self.cache[key]
                node.value = value
                self.remove_from_list(node)
                self.add_to_top(node)
        else:
            if key not in self.cache:
                tbr_key = self.take_out_last()
                del self.cache[tbr_key]
                node = Node(key,value)
                self.cache[key] = node
                self.add_to_top(node)
            else:
                node = self.cache[key]
                node.value = value
                self.remove_from_list(node)
                self.add_to_top(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)