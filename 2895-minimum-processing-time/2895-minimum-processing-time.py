class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        n = len(processorTime)
        mx_time = 0
        for i in range(n):
            time = 0
            for j in range(4):
                time = processorTime[i] + tasks[(i)*4 + j]        
                if time > mx_time:
                    mx_time = time
        
        return mx_time

        