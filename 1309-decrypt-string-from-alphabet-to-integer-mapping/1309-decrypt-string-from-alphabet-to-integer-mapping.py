class Solution:
    def freqAlphabets(self, s: str) -> str:
        # ord('a') and chr(97)
        output = ''
        j = 0
        while j < len(s):
            hashtag = j + 2
            if hashtag < len(s):
                if s[hashtag] == '#':
                    output += chr(int(s[j:j+2]) -1 + ord('a'))
                    j = hashtag + 1
                    continue
            output += chr(int(s[j])-1 + ord('a'))
            j += 1

        return output

