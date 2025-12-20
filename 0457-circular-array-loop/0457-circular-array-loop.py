class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        def next_idx(ptr): 
            return (ptr + nums[ptr])%len(nums)

        for i in range(len(nums)): 
            if i in visited: 
                continue
            slow, fast = i, i
            direction = nums[i]
            while True: 
                visited.add(slow)
                visited.add(fast)
                if direction * nums[slow] < 0 or direction * nums[fast] < 0: 
                    break 
                slow = next_idx(slow)
                fast = next_idx(fast)

                if direction * nums[fast]<0: 
                    break
                fast = next_idx(fast)
                if slow == fast: 
                    if slow == next_idx(slow): 
                        break
                    return True 



        return False
            
