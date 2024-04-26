class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for ele in logs:
            if ele[1] == '.': 
                if stack:
                    stack.pop()
            elif ele == './':
                continue
            else:
                stack.append(1)
        
        return len(stack)