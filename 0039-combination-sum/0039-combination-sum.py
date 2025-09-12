class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, total, combination): 
            if total == target: 
                res.append(list(combination))
                return 
            if total > target: 
                return

            for i in range(start, len(candidates)): 
                combination.append(candidates[i])
                backtrack(i, total + candidates[i], combination)
                combination.pop()
        
        backtrack(0, 0, [])
        return res
            
