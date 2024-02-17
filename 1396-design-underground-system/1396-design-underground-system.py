from collections import deque

class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.check_out = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_in:
            self.check_in[id].append({'name': stationName, 'st': t})
        else:
            stack = deque()
            stack.append({'name': stationName, 'st': t})
            self.check_in[id] = stack

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        user_data = self.check_in[id].pop()
        
        start_name = user_data['name']
        start_time = user_data['st']
        elapsed = t - start_time

        string = f'{start_name}-{stationName}'

        if string in self.check_out:
            self.check_out[string].append(elapsed)
        else:
            self.check_out[string] = [elapsed]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        string = f'{startStation}-{endStation}'
        lst = self.check_out[string]
        
        return sum(lst) / len(lst)

        

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)