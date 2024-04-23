class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        digit = ''
        for c in s:
            if c == '[':
                stack.append(digit)
                digit = ''
                continue
            elif c != ']' and not c.isdigit():
                stack.append(c)
            elif c.isdigit():
                digit += c
            else:
                acc = stack.pop()
                cur = stack.pop()
                while not cur.isdigit():
                    acc = cur + acc
                    cur = stack.pop()
    
                stack.append(acc * int(cur))
            print(stack)
        return ''.join(stack)

                