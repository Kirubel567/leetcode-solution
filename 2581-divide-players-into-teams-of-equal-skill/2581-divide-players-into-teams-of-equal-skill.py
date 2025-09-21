class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left, right, ans = 0, len(skill) -1 , 0

        startingSum = skill[left] + skill[right]

        while left < right: 
            prod = skill[left] * skill[right]
            if(skill[left] + skill[right] == startingSum):
                ans += prod
            else: 
                return -1
            left += 1
            right -= 1
        
        return ans 