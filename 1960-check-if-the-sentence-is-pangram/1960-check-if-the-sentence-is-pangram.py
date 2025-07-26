class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mapp = dict()
        for i in range(len(sentence)): 
            mapp[sentence[i]] = mapp.get(sentence[i], 0) + 1
        
        return len(mapp) == 26