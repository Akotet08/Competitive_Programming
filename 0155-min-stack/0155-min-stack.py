class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if self.stack:
            min_val, old_val = self.stack[-1]

            if val < min_val:
                self.stack.append((val, val))
            else:
                self.stack.append((min_val, val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        _, val = self.stack.pop()
        return val
        
    def top(self) -> int:
        _, val = self.stack[-1]
        return val

    def getMin(self) -> int:
        val, _ = self.stack[-1]
        return val
    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()