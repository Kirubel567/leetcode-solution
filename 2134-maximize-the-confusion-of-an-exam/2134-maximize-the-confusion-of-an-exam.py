class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #we need to count the number of trues and false's then if their number in that substring is less than or equal to k, then we add the window

        l, ans, window = 0, -float('inf'), 0
        count = defaultdict(int)

        for right in range(len(answerKey)): 
            count[answerKey[right]] += 1
            window += 1

            while window - max(count.values()) > k: 
                count[answerKey[l]] -= 1
                l+= 1
                window -= 1
            ans = max(window, ans)
                
        return ans 