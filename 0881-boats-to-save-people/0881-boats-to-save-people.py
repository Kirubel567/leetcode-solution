class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right, count = 0, len(people)-1, 0
        people.sort()

        while left <= right: 
            if people[left] + people[right] <= limit: 
                left += 1
                

            right -=1
            count += 1
        return count 