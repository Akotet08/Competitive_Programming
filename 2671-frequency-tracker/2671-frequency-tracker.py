class FrequencyTracker:

    def __init__(self):
        self.tracker = {}
        self.freq = {}

    def add(self, number: int) -> None:
        if number in self.tracker and self.tracker[number] != 0 :
            prev_freq = self.tracker[number]
            self.tracker[number] += 1
            self.freq[prev_freq] -= 1

            new_freq = self.tracker[number]
            if new_freq in self.freq:
                self.freq[new_freq] += 1
            else:
                self.freq[new_freq] = 1
            
        else:
            self.tracker[number] = 1
            if 1 in self.freq:
                self.freq[1] += 1
            else:
                self.freq[1] = 1
        
    def deleteOne(self, number: int) -> None:
        if number in self.tracker and self.tracker[number] != 0:
            self.freq[self.tracker[number]] -= 1
            self.tracker[number] -= 1

            new_freq = self.tracker[number]
            if new_freq in self.freq:
                self.freq[new_freq] += 1
            else:
                self.freq[new_freq] = 1

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq and self.freq[frequency] != 0:
            return True 
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)