class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        total_pts = sum(cardPoints)
        ans = -float('inf')
        Sum = 0

        for i in range(window_size): 
            Sum += cardPoints[i]
        
        ans = max(total_pts - Sum, ans)
        tracker = 0
        for i in range(len(cardPoints)-k, len(cardPoints)):
            Sum -= cardPoints[tracker]
            Sum += cardPoints[i]
            tracker += 1

            ans = max(total_pts - Sum, ans)

        return ans
