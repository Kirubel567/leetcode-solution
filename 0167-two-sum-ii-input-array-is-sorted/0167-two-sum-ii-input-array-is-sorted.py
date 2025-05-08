class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            Sum = numbers[left] + numbers[right]

            if Sum == target:
                arr += [left + 1]
                arr += [right + 1]
                return arr
            elif Sum < target:
                left += 1
            elif Sum > target: 
                right -= 1

        return arr


