class RecentCounter:

    def __init__(self):
        self.holder = deque()
        # self.high, self.low = 0, 0

    def ping(self, t: int) -> int:
        self.holder.append(t)
        low = t-3000
        high = t

        while self.holder and self.holder[0] < low or self.holder[0] > t: 
            self.holder.popleft()
        
        return len(self.holder)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentselfCounter()
# param_1 = obj.ping(t)