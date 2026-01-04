class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        #every number has two devisors by default
        #find the divisors of each numbers that are less than sqrt(nums[i])
        #iterate trough the numbers and if the number of devisors until sqrt(nums[i]) is exactly two return true else false

        totalSum = 0
        for i in range(len(nums)): 
            localSum, count = 0, 0
            print(int(sqrt(nums[i])))
            for j in range(1, int(sqrt(nums[i]))+1): 
                if nums[i]%j == 0: 
                    if j == nums[i] // j:
                        localSum += j
                        count += 1
                    else:
                        localSum += j + nums[i] // j
                        count += 2
                    if count > 4: 
                        break 
            
            if count == 4: 
                totalSum += localSum
        return totalSum
