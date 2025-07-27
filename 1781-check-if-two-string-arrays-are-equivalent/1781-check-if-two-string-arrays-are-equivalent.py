class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wordOne = ''.join(word1)
        wordTwo = ''.join(word2)

        return wordOne == wordTwo