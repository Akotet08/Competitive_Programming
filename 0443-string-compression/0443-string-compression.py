class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        pos = 0
        while i < len(chars):
            cur = chars[i]
            count = 0
            while i< len(chars) and chars[i] == cur:
                count += 1
                i += 1
            if count > 1:
                chars[pos] = cur
                if count < 10:
                    chars[pos + 1] = str(count)
                    pos += 2
                else:
                    l = str(count)
                    for j in range(len(l)):
                        chars[pos + 1 + j] = l[j]
                    pos += len(l) + 1
            else:
                chars[pos] = cur
                pos += 1
        return pos
