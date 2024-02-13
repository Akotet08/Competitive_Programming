class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')

        res = []
        for word in words:
            s = set(word.lower())
            if s.issubset(first_row) or s.issubset(second_row) or s.issubset(third_row):
                res.append(word)
        return res

        