class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        main_stack = []
        count = 0

        for c in s:
            if c == '(':
                main_stack.append(0)
            else:
                val = main_stack.pop()
                value = max(1, 2*val)
                
                if len(main_stack) == 0:
                    count += value
                else:
                    main_stack[-1] += value
        return count
        