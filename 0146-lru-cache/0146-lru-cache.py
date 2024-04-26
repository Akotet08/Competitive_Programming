class LRUCache:

    def __init__(self, capacity: int):
        self.mapp = {}
        self.queue = deque()
        self.size = capacity
        self.count = 0
    def get(self, key: int) -> int:
        if key in self.mapp:
            self.queue.remove(key)
            self.queue.append(key)
            return self.mapp[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.mapp:
            self.get(key)
            self.mapp[key] = value

            return
            
        if self.count >= self.size:
            k = self.queue.popleft()
            del self.mapp[k]         
        self.queue.append(key)
        self.mapp[key] = value
        
        self.count += 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)