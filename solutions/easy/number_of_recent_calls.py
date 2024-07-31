class RecentCounter:

    def __init__(self):
        self.x = []

    def ping(self, t: int) -> int:
        self.x.append(t)
        l = [t-3000,t]
        while self.x and min(self.x) < l[0]:
            temp = []
            for i in self.x:
                if i >= l[0]:
                    temp.append(i)
            self.x = temp  
        return len(self.x)
        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)