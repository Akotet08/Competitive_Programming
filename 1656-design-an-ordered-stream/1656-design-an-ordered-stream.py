class OrderedStream:

    def __init__(self, n: int):
        self.lst = [0] * n
        self.idx = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey - 1] = value
        lst = []
        if self.lst[self.idx] == 0:
            return []
        while self.idx < self.n and self.lst[self.idx] !=0:
            lst.append(self.lst[self.idx])
            self.idx += 1
        
        return lst


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)