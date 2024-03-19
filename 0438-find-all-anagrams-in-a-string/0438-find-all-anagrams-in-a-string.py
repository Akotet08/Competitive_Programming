class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        target = Counter(p)
        window = Counter(s[:l])
        lst = []
        
        i = 1
        while i + l -1 < len(s):
            if window == target:
                lst.append(i - 1)
            print(i, window)

            prev = s[i - 1]
            if window[prev] == 1:
                del window[prev]
            else:
                window[prev] -= 1
            
            nxt = s[i + l -1]
            if nxt in window:
                window[nxt] += 1
            else:
                window[nxt] = 1

            i += 1

        if window == target:
            lst.append(i-1)
        return lst
