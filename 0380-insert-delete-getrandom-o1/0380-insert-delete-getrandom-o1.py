import random 

class RandomizedSet:

    def __init__(self):
        self.items = {}
        self.item_list = []

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items[val] = len(self.item_list)
        self.item_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.items:
            return False
        
        idx = self.items[val]
        if idx == len(self.item_list):
            self.item_list.pop()
        else:
            self.item_list[idx], self.item_list[-1] = self.item_list[-1], self.item_list[idx]
            self.item_list.pop()
        self.items.pop(val)
        return True
        
    def getRandom(self) -> int:
        return random.sample(self.item_list, 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()