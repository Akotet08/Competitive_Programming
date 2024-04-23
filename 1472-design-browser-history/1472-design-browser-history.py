class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = 0
        self.history = [homepage] 

    def visit(self, url: str) -> None:
        self.current += 1
        del self.history[self.current: ]

        self.history.append(url)
    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]
        
    def forward(self, steps: int) -> str:
        n = len(self.history) - 1 
        self.current = min(n, self.current + steps)
        return self.history[self.current]
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)