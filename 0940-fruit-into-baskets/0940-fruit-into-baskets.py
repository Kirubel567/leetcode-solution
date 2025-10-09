class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left, window, res = 0, 0, 0

        for r in range(len(fruits)): 
            count[fruits[r]] += 1
            window += 1
            
            while len(count) > 2: 
                count[fruits[left]] -= 1
                window -=1
                if not count[fruits[left]]:                     
                    count.pop(fruits[left])
                left += 1
            res = max(res, window)

        return res 

