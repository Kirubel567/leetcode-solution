class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected= sorted(heights)

        count = 0
        for current, expected in zip(heights, expected): 
            if current != expected: 
                count +=1
        return count 