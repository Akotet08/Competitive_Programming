import random 

class RandomizedSet:

    def __init__(self):
        self.items = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.items:
            return False
        idx = self.items[val]
        lst_element = self.list[-1]

        self.list[idx] = self.list[-1]

        self.items[lst_element] = idx
        self.list.pop()

        del self.items[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()