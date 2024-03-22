class RecentCounter:

    def __init__(self):
        self.line = []

    def ping(self, t: int) -> int:
        i = 0
        while (i < len(self.line) and t - self.line[i] > 3000):
            i += 1
        self.line = self.line[i:]
        self.line.append(t)
        return len(self.line)
    

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)