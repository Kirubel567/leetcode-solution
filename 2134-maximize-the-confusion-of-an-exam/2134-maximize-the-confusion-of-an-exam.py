class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #we need to count the number of trues and false's then if their number in that substring is less than or equal to k, then we add the window

        window = 0
        count = {"T":0, "F":0}

        for i in range(len(answerKey)): 
            count[answerKey[i]] += 1
            minimum = min(count["T"], count["F"])

            if minimum <= k: 
                window +=1
            else: 
                count[answerKey[i - window]] -= 1
            
        return window