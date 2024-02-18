import random 

class RandomizedSet:

    def __init__(self):
        self.items = {}

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items[val] = 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.items:
            return False
        self.items.pop(val)
        return True
        
    def getRandom(self) -> int:
        return random.sample(list(self.items.keys()), 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()