class LRUCache:
    def __init__(self, capacity: int):
        self.limit = capacity
        self.capacity = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.capacity:
            self.capacity.move_to_end(key)
            return self.capacity[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.capacity:
            del self.capacity[key]

        self.capacity[key] = value

        if len(self.capacity) > self.limit:
            self.capacity.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
