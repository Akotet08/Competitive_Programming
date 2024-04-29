class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queue = deque()
        max_len = 0

        for ele in nums:
            while queue and abs(queue[0] - ele) > limit:
                queue.popleft()
            queue.append(ele)
            max_len = max(max_len, len(queue))            
        return max_len
