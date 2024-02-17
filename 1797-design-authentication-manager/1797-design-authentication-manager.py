class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.dic = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId] = currentTime + self.timeToLive
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if not tokenId in self.dic:
            return
        token_time = self.dic[tokenId]
        if currentTime < token_time:
            self.dic[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.dic:
            if currentTime < self.dic[token]:
                count += 1
        return count

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)