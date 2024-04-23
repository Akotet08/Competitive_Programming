class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_char = set(['(', '{', '[' ])
        close_char = set([')', '}', ']'])

        match = {'(' : ')', '{': '}', '[' : ']'}

        for c in s:
            if c in open_char:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                op = stack.pop()
                if match[op] != c:
                    return False
        
        return len(stack) == 0
