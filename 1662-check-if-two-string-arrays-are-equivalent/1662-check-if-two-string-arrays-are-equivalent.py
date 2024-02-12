class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        frst_str = ''.join(word1)
        scnd_str = ''.join(word2)

        return frst_str == scnd_str
        